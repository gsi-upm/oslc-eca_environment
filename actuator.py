from models.actions import Action
from rdflib import Graph, Namespace, Literal, BNode, RDF, DCTERMS
from rdflib.resource import Resource
import requests

EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')
OSLC = Namespace('http://open-services.net/ns/core#')
OSLC_CM = Namespace('http://open-services.net/ns/cm#')
ROI = Namespace('http://gsi.upm.es/ontologies/roi/')

def execute_actions(actions):
    g = Graph()
    g.parse(data=actions, format='n3')

    for subject in g.subjects(RDF.type, EWE.Action):
        action = Action()

        for triple in g.triples((subject, None, None)):
            action.rdf.add(triple)
            execute(action)


def execute(action):
    resource = action.get_resource()
    query = action.get_query()
    # serviceProvider requests.get(action.get_service_provider(), auth=)
    
    for action_type in g.objects(action, RDF.type):

        if action_type == ROI.CreateResource:
            return
            

            # print('\nCreate Resource action executes')
            # create_resource(serviceProvider, properties)

        # elif action_type == ROI.UpdateResource:                
            
        #     serviceProvider = properties.value(OSLC.serviceProvider)

        #     print('\nUpdate Resource action executes')
        #     update_resource(serviceProvider, query, properties)

        # elif action_type == ROI.DeleteResource:

        #     serviceProvider = query.value(OSLC.serviceProvider)
            
        #     print('\nDelete Resource action executes')
        #     delete_resource(serviceProvider, query)
    

def create_resource(serviceProvider, properties):

    # for param in parameters:
    #     print(param)
    #     # TODO: use service provider
    #     print(param.value(RDF.type))
    #     if param.value(RDF.type).identifier == EWE.ResourceURI:
    #         uri = param.value(RDF.value)
    #         print(uri)

    # g = Graph()
    # for p, o in resource.predicate_objects():
    #     if p.identifier == DCTERMS.contributor:
    #         o = Literal('GuillermoGarcia96')
    #     if type(o) == Resource:
    #         o = o.identifier
    #     g.add((resource.identifier, p.identifier, o))
    
    # g.add((resource.identifier, DCTERMS.description, Literal("example")))

    # data = g.serialize(format='turtle')
    # print(data.decode('utf-8'))
    # requests.post(uri, auth=('', ''), headers={'Content-type': 'text/turtle', 'Accept': 'text/turtle'}, data=data)
    
    return

def update_resource(serviceProvider, query, properties):
    return

def delete_resource(serviceProvider, query):
    return


def get_service_provider(uri):
    requests.get(str(uri))
    return

# class ServiceProvider:
#     def __init__(self):
