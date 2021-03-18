from rdflib import Graph, Namespace, Literal, RDF, DCTERMS
from rdflib.resource import Resource
import requests

EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')
OSLC_CM = Namespace('http://open-services.net/ns/cm#')

def actuator(response):
    g = Graph()
    g.parse(data=response, format='n3')

    for s in g.subjects(RDF.type, EWE.Action):
        action = Resource(g, s)
    
    for s in g.subjects(RDF.type, OSLC_CM.ChangeRequest):
        resource = Resource(g, s)
    
    for o in action.objects():
        if o.identifier == EWE.CreateResource:
            print('Create Resource action executes')
            parameters = action.objects(EWE.hasParameter)
            create_resource(parameters, resource)

        if o.identifier == EWE.UpdateResource:
            print('Update Resource action executes')
            parameters = action.objects(EWE.hasParameter)
            update_resource(parameters, resource)

        if o.identifier == EWE.DeleteResource:
            print('Delete Resource action executes')
            parameters = action.objects(EWE.hasParameter)
            delete_resource(parameters, resource)
    
    return


def create_resource(parameters, resource):
    for param in parameters:
        print(param)
        # TODO: use service provider
        print(param.value(RDF.type))
        if param.value(RDF.type).identifier == EWE.ResourceURI:
            uri = param.value(RDF.value)
            print(uri)

    g = Graph()
    for p, o in resource.predicate_objects():
        if p.identifier == DCTERMS.contributor:
            o = Literal('GuillermoGarcia96')
        if type(o) == Resource:
            o = o.identifier
        g.add((resource.identifier, p.identifier, o))
    
    g.add((resource.identifier, DCTERMS.description, Literal("example")))

    data = g.serialize(format='turtle')
    print(data.decode('utf-8'))
    requests.post(uri, auth=('', ''), headers={'Content-type': 'text/turtle', 'Accept': 'text/turtle'}, data=data)
    
    return

def update_resource(parameters, resource):
    return

def delete_resource(parameters, resource):
    return