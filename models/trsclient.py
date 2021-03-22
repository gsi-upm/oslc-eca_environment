import requests
from rdflib import Graph, Namespace, BNode, URIRef
from rdflib.namespace import RDFS, RDF
from rdflib.resource import Resource

TRS = Namespace('http://open-services.net/ns/core/trs#')
LDP = Namespace('http://www.w3.org/ns/ldp#')

class TRSClient:
    def __init__(self, uri, username, password, channel):
        self.rdf = Graph()
        self.credentials = (username, password)
        self.uri = uri
        self.channel = channel


    def initialize(self):
        base_uri = self.__get_uri_base()

        while base_uri:
            base_uri = self.__add_resources(base_uri)
        
        return


    def incremental_update(self, create_callback=None, update_callback=None, delete_callback=None):
        change_log = []
        change_log_uri = self.uri

        while change_log_uri:
            change_log_uri = self.__find_sync_point(change_log_uri, change_log)
        
        self.__apply_resource_changes(change_log, create_callback, update_callback, delete_callback)

        return


    def __get_uri_base(self):
        response = requests.get(self.uri, auth=self.credentials, headers={'Accept': 'application/rdf+xml'})

        graph = Graph()
        graph.parse(data=response.content, format='xml')

        for uri in graph.objects(None, TRS.base):
            return uri.toPython()

        return ''


    def __add_resources(self, base_uri):
        response = requests.get(base_uri, auth=self.credentials, headers={'Accept': 'application/rdf+xml'})

        graph = Graph()
        graph.parse(data=response.content, format='xml')

        if (None, TRS.cutoffEvent, None) in graph:
            for sync_point in graph.triples((None, TRS.cutoffEvent, None)):
                self.rdf.add(sync_point)

        for resource in graph.objects(None, LDP.member): # WTF: en el adaptador de bugzilla es RDFS.member
            response = requests.get(resource.toPython(), auth=self.credentials, headers={'Accept': 'application/rdf+xml'})
            self.rdf.parse(data=response.content, format='xml')
            self.rdf.add((URIRef('_:resourceSet'), URIRef('_:hasResource'), resource))
        
        if (None, LDP.nextPage, RDF.nil) in graph:
            return ''

        else:
            for next_uri in graph.objects(None, LDP.nextPage):
                return next_uri.toPython()


    def __find_sync_point(self, uri, change_log):
        response = requests.get(uri, auth=self.credentials, headers={'Accept': 'text/turtle'})

        graph = Graph()
        graph.parse(data=response.content, format='turtle')

        # TODO: use Resource from rdflib
        query = graph.query("""
            PREFIX trs: <http://open-services.net/ns/core/trs#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

            SELECT ?change ?resource ?action

            WHERE {
                ?change trs:order ?order .
                ?change trs:changed ?resource .
                ?change rdf:type ?action .
            }

            ORDER BY DESC(?order)
        """)

        for change, resource, action in query:
            if (None, TRS.cutoffEvent, change) in self.rdf:
                return ''
            else:
                change_log.insert(0, {"change": change, "resource": resource, "action": action})

        if (None, TRS.previous, RDF.nil) in graph:
            change_log.clear()
            return ''

        else:
            for previous_uri in graph.objects(None, TRS.previous):
                return previous_uri


    def __apply_resource_changes(self, change_log, create_callback=None, update_callback=None, delete_callback=None):
        for event in change_log:
            if event["action"] == TRS.Creation:

                print("Creating: "+str(event['resource']))

                response = requests.get(str(event["resource"]), auth=self.credentials, headers={'Accept': 'application/rdf+xml'})
                self.rdf.parse(data=response.content, format='application/rdf+xml')

                # Send event to EWE Tasker
                if create_callback:
                    create_callback(self.rdf.triples((event['resource'], None, None)))

                self.rdf.add((URIRef('_:resourceSet'), URIRef('_:hasResource'), event["resource"]))

                
            elif event["action"] == TRS.Modification:

                previous_resource = Graph()
                for triple in self.rdf.triples((event['resource'], None, None)):
                    previous_resource.add(triple)

                print("Updating: "+str(event['resource']))
                
                self.rdf.remove((event["resource"], None, None))
                response = requests.get(str(event["resource"]), auth=self.credentials, headers={'Accept': 'application/rdf+xml'})
                self.rdf.parse(data=response.content, format='application/rdf+xml')

                # Send event to EWE Tasker
                if update_callback:
                    update_callback(self.rdf.triples((event['resource'], None, None)), previous_resource)

                self.rdf.add((URIRef('_:resourceSet'), URIRef('_:hasResource'), event["resource"]))


            elif event["action"] == TRS.Deletion:

                previous_resource = Graph()
                for triple in self.rdf.triples((event['resource'], None, None)):
                    previous_resource.add(triple)

                print("Deleting: "+str(event['resource']))

                # Send event to EWE Tasker
                if delete_callback:
                    delete_callback(previous_resource)

                self.rdf.remove((event["resource"], None, None))


            else:
                continue
        
            self.rdf.remove((None, TRS.cutoffEvent, None))
            self.rdf.add((BNode(), TRS.cutoffEvent, event["change"]))

        return