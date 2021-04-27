from rdflib import Graph, URIRef, Namespace, Literal, BNode, RDF, RDFS, FOAF
from rdflib.resource import Resource
import requests

ROI = Namespace('http://gsi.upm.es/ontologies/roi/')
EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')
OSLC_CM = Namespace('http://open-services.net/ns/cm#')
OSLC = Namespace('http://open-services.net/ns/core#')


class Event:
    def __init__(self, event_type):
        self.rdf = Graph()
        self.uri = ROI['event'+str(id(self))]

        self.parameters = []

        self.rdf.add((self.uri, RDF.type, EWE.Event))
        self.rdf.add((self.uri, RDF.type, event_type))
        self.rdf.add((self.uri, RDFS.label, Literal('Event')))
        self.rdf.add((self.uri, RDFS.comment, Literal('Event')))

    def add_channel(self, channel):
        self.rdf.add((self.uri, EWE.isGeneratedBy, channel))

    def add_parameter(self, param):
        self.parameters.append(param)
        self.rdf.add((self.uri, EWE.hasParameter, param.uri))

    def get_rdf(self):
        g = Graph()
        g += self.rdf
        for p in self.parameters:
            g += p.rdf
        return g.serialize(format='n3').decode('utf-8')


class Action:
    def __init__(self):
        self.rdf = Graph()

    def get_resource(self):

        resource = Graph()
        resource_uri = BNode()

        for properties in self.rdf.subjects(RDF.type, ROI.ResourceProperties):
            for (p, o) in self.rdf.predicate_objects(properties):
                if p != RDF.type:
                    resource.add((resource_uri, p, o))

        resource.add((resource_uri, RDF.type, OSLC_CM.ChangeRequest))

        return resource

    # Improvement: URL encoded requests
    def get_query(self):

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

    def get_service_provider(self, credentials):
        uri = next(str(uri) for uri in self.rdf.objects(None, OSLC.serviceProvider))

        serviceProvider = requests.get(uri, auth=credentials, headers={'Accept': 'text/n3'}).content

        g = Graph()
        g.parse(data=serviceProvider, format='n3')

        return g


class QueryProperties:
    def __init__(self):
        self.rdf = Graph()
        self.uri = BNode()

        self.properties = []

        self.rdf.add((self.uri, RDF.type, EWE.Parameter))
        self.rdf.add((self.uri, RDF.type, ROI.QueryProperties))
        self.rdf.add((self.uri, RDFS.label, Literal('QueryProperties')))
        self.rdf.add((self.uri, RDFS.comment, Literal('QueryProperties')))
        self.rdf.add((self.uri, RDFS.domain, ROI.OSLCServer))

    def add(self, rdftype, rdfvalue):
        self.rdf.add((self.uri, rdftype, rdfvalue))

        self.properties.append({'type': rdftype, 'value': rdfvalue})


class ResourceProperties:
    def __init__(self):
        self.rdf = Graph()
        self.uri = BNode()

        self.properties = []

        self.rdf.add((self.uri, RDF.type, EWE.Parameter))
        self.rdf.add((self.uri, RDF.type, ROI.ResourceProperties))
        self.rdf.add((self.uri, RDFS.label, Literal('ResourceProperties')))
        self.rdf.add((self.uri, RDFS.comment, Literal('ResourceProperties')))
        self.rdf.add((self.uri, RDFS.domain, ROI.OSLCServer))

    def add(self, rdftype, rdfvalue):
        self.rdf.add((self.uri, rdftype, rdfvalue))

        self.properties.append({'type': rdftype, 'value': rdfvalue})
    
        