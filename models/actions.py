from rdflib import Graph, URIRef, Namespace, Literal, BNode, RDF, RDFS
from rdflib.resource import Resource
import requests

ROI = Namespace('http://gsi.upm.es/ontologies/roi/')
EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')
OSLC_CM = Namespace('http://open-services.net/ns/cm#')
OSLC = Namespace('http://open-services.net/ns/core#')


class ActionQueue:
    def __init__(self):
        self.actions = []

    def add(self, data):
        g = Graph()
        g.parse(data=data, format='n3')

        for subject in g.subjects(RDF.type, EWE.Action):
            action = Action()

            for triple in g.triples((subject, None, None)):
                action.rdf.add(triple)

            for param in g.objects(subject, EWE.hasParameter):
                for triple in g.triples((param, None, None)):
                    action.rdf.add(triple)
            
            self.actions.append(action)

class Action:
    def __init__(self):
        self.rdf = Graph()

    def set_credentials(self, step):
        for output in step.output:
            if output.uri in self.rdf.objects(None, EWE.isProvidedBy):
                self.credentials = (output.user, output.password)

    def execute(self):

        for action_type in self.rdf.objects(None, RDF.type):
            if action_type == ROI.CreateResource:
                return self.__create()

            elif action_type == ROI.UpdateResource:
                return self.__update()

            elif action_type == ROI.CreDeleteResource:
                return self.__delete()

        return

    def __create(self):
        serviceProvider = self.__get_service_provider(self.credentials)
        resource = self.__get_resource()

        creation_uri = next(uri for uri in serviceProvider.objects(None, OSLC.creation))
        payload = resource.serialize(format='turtle')

        print('\nCreating resource:\n')
        print(payload.decode('utf-8'))

        return requests.post(creation_uri, auth=self.credentials, data=payload, headers={'Content-type': 'text/turtle'})


    def __update(self):
        serviceProvider = self.__get_service_provider(self.credentials)
        resource = self.__get_resource()
        query = self.__get_query()

        query_uri = next(uri for uri in serviceProvider.objects(None, OSLC.queryBase))

        data = requests.get(query_uri, auth=self.credentials, headers={'Accept': 'text/n3'}).content
        resource_list = Graph()
        resource_list.parse(format='n3', data=data)
        print(resource_list.serialize(format='n3').decode('utf-8'))
        print(query)

        update_uri = next(result.uri for result in resource_list.query(query))
        payload = resource.serialize(format='turtle')

        print('\nUpdating resource:\n')
        print(payload.decode('utf-8'))

        return requests.put(update_uri, auth=self.credentials, data=payload, headers={'Content-type': 'text/turtle'})


    def __delete(self):
        serviceProvider = self.__get_service_provider(self.credentials)
        query = self.__get_query()

        query_uri = next(uri for uri in serviceProvider.objects(None, OSLC.queryBase))

        data = requests.get(query_uri, auth=self.credentials, headers={'Accept': 'text/n3'}).content
        resource_list = Graph()
        resource_list.parse(format='n3', data=data)

        delete_uri = next(result.uri for result in resource_list.query(query))
        print('\nDeleting resource:\n')

        return requests.delete(delete_uri, auth=self.credentials)


    def __get_resource(self):

        resource = Graph()
        resource_uri = BNode()

        for properties in self.rdf.subjects(RDF.type, ROI.ResourceProperties):
            for (p, o) in self.rdf.predicate_objects(properties):
                if p != RDF.type:
                    resource.add((resource_uri, p, o))

        resource.add((resource_uri, RDF.type, OSLC_CM.ChangeRequest))

        return resource

    def __get_query(self):

        query = """
            select ?uri
            where {
        """

        for properties in self.rdf.subjects(RDF.type, ROI.QueryProperties):
            for (p, o) in self.rdf.predicate_objects(properties):
                if p == RDF.type:
                    continue
                query += "?uri {} {} .\n".format(p.n3(), o.n3())

        query += "}"

        return query

    def __get_service_provider(self, credentials):
        uri = next(str(uri) for uri in self.rdf.objects(None, OSLC.serviceProvider))

        serviceProvider = requests.get(uri, auth=credentials, headers={'Accept': 'text/n3'}).content

        g = Graph()
        g.parse(data=serviceProvider, format='n3')

        return g

    
        