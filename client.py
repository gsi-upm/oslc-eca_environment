import requests
from rdflib import Graph, Namespace
from rdflib.namespace import RDFS, RDF

TRS = Namespace('http://open-services.net/ns/core/trs#')
LDP = Namespace('http://www.w3.org/ns/ldp#')

def initialize(trs_uri, credentials, store):
    base_uri = get_uri_base(trs_uri, credentials)

    while base_uri:
        base_uri = add_resources(base_uri, credentials, store)
    
    print(store.serialize(format='n3', indent=2).decode('ascii'))
    return 1


def get_uri_base(uri, credentials):
    response = requests.get(uri, auth=credentials, headers={'Accept': 'application/rdf+xml'})

    graph = Graph()
    graph.parse(data=response.content, format='xml')

    for uri in graph.objects(None, TRS.base):
        return uri.toPython()

    return ''


def add_resources(base_uri, credentials, store):
    response = requests.get(base_uri, auth=credentials, headers={'Accept': 'application/rdf+xml'})

    graph = Graph()
    graph.parse(data=response.content, format='xml')

    if (None, TRS.cutoffEvent, None) in graph:
        for syncPoint in graph.triples((None, TRS.cutoffEvent, None)):
            store.add(syncPoint)

    for resource in graph.objects(None, RDFS.member):
        response = requests.get(resource.toPython(), auth=credentials, headers={'Accept': 'application/rdf+xml'})
        store.parse(data=response.text, format='xml')
    
    if (None, LDP.nextPage, RDF.nil) in graph:
        return ''

    for next_uri in graph.objects(None, LDP.nextPage):
        return next_uri.toPython()

    return ''


def incremental_update(trs_uri, credentials, store):
    
    return 1