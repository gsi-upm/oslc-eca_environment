from rdflib import Graph, URIRef, Namespace, Literal, BNode, RDF, RDFS, FOAF
from rdflib.resource import Resource

ROI = Namespace('http://gsi.upm.es/ontologies/roi/')
EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')


class EventQueue:
    def __init__(self):
        self.events = []

    def new_create_event(self, resource):
        event = Event(ROI.ResourceCreated)
        param = ResourceProperties()

        for (s, p, o) in resource:
            param.add(p, o)

        event.add_parameter(param)
        self.events.append(event)


    def new_update_event(self, resource, previous_resource):
        event = Event(ROI.ResourceUpdated)
        param1 = ResourceProperties()
        param2 = QueryProperties()

        for (s, p, o) in resource:
            param1.add(p, o)
        
        for (s, p, o) in previous_resource:
            param2.add(p, o)

        event.add_parameter(param1)
        event.add_parameter(param2)
        self.events.append(event)


    def new_delete_event(self, previous_resource):
        event = Event(ROI.ResourceDeleted)
        param = QueryProperties()

        for (s, p, o) in previous_resource:
            param.add(p, o)

        event.add_parameter(param)
        self.events.append(event)


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