from rdflib import Graph, URIRef, Namespace, Literal, RDF, FOAF
from rdflib.resource import Resource

ROI = Namespace('http://www.gsi.upm.es/ontologies/roi/')
EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')

class Workflow:
    def __init__(self):
        self.rdf = Graph()
        self.uri = ROI['workflow'+str(id(self))]

        self.rdf.add((self.uri, RDF.type, ROI.Workflow))

    def display(self):
        print(self.rdf.serialize(format='n3').decode('utf-8'))

    def create_steps(self, n):
        self.steps = []
        self.rdf.add((self.uri, ROI.numberOfSeps, Literal(n)))

        for i in range(0, n):
            step = Step(i+1)
            self.rdf.add((self.uri, ROI.hasStep, step.uri))
            self.steps.append(step)


class Step:
    def __init__(self, order):
        self.rdf = Graph()
        self.uri = ROI['step'+str(id(self))]
        self.user = User('step'+str(id(self))+'user', '')
        
        self.order = order

        self.input = []
        self.output = []
        self.rules = []

        self.rdf.add((self.uri, RDF.type, ROI.Step))
        self.rdf.add((self.uri, ROI.order, Literal(order)))
        self.rdf.add((self.uri, ROI.actsAsUser, self.user.uri))

    def display(self):
        print(self.rdf.serialize(format='n3').decode('utf-8'))

    def add_input(self, oslc_server):
        self.rdf.add((self.uri, ROI.getsInputFrom, oslc_server.uri))
        self.input.append(oslc_server)

    def add_output(self, oslc_server):
        self.rdf.add((self.uri, ROI.sendsOutputTo, oslc_server.uri))
        self.output.append(oslc_server)

    def add_rule(self, rule):
        self.rdf.add((self.uri, ROI.triggersRule, rule.uri))
        self.rules.append(rule)


class User:
    def __init__(self, username, password):
        self.rdf = Graph()
        self.uri = EWE[username]
        self.username = username
        self.password = password

        self.rdf.add((self.uri, RDF.type, EWE.User))
        self.rdf.add((self.uri, FOAF.accountName, Literal(username)))


class OSLCServer:
    def __init__(self, name, oslc, trs, user, password):
        self.rdf = Graph()
        self.uri = ROI['oslcServer'+name]
        self.name = name
        self.oslc = oslc
        self.trs = trs
        self.user = user
        self.password = password

        self.rdf.add((self.uri, RDF.type, EWE.Channel))
        self.rdf.add((self.uri, RDF.type, ROI.OSLCServer))
        self.rdf.add((self.uri, ROI.usesProvider, URIRef(oslc)))
        self.rdf.add((self.uri, ROI.usesTracker, URIRef(trs)))

    def display(self):
        print(self.rdf.serialize(format='n3').decode('utf-8'))


class Rule:
    def __init__(self, user):
        self.rdf = Graph()
        self.uri = ROI['rule'+str(id(self))]
        self.user = user

        self.rdf.add((self.uri, RDF.type, EWE.Rule))
        self.rdf.add((self.uri, EWE.hasCreator, user))

    def display(self):
        print(self.rdf.serialize(format='n3').decode('utf-8'))

    def set_value(self, rule):
        self.value = rule
        self.rdf.add((self.uri, RDF.value, Literal(rule)))