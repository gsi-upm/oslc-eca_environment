from rdflib import Graph, URIRef, Namespace, Literal, BNode, RDF, RDFS
from rdflib.resource import Resource
from models import Event, Action, ResourceProperties, QueryProperties
import requests

ROI = Namespace('http://gsi.upm.es/ontologies/roi/')
EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')
OSLC_CM = Namespace('http://open-services.net/ns/cm#')
OSLC = Namespace('http://open-services.net/ns/core#')


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