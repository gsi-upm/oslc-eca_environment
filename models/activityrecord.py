from rdflib import Graph, URIRef, Namespace, Literal, BNode, RDF, RDFS, FOAF
from rdflib.resource import Resource

ROI = Namespace('http://gsi.upm.es/ontologies/roi/')
EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')

class ActivityRecord:
    def __init__(self):
        self.rdf = Graph()
        self.uri = ROI['activityRecord'+str(id(self))]

        self.events = []
        self.actions = []

        self.rdf.add((self.uri, RDF.type, ROI.ActivityRecord))