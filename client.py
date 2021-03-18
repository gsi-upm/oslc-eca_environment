import requests
import time
from rdflib import Graph, Namespace, BNode, URIRef
from rdflib.namespace import RDFS, RDF
from ewe import evaluate

TRS = Namespace('http://open-services.net/ns/core/trs#')
LDP = Namespace('http://www.w3.org/ns/ldp#')

def initialize(trs_uri, credentials, store):
    base_uri = get_uri_base(trs_uri, credentials)

    while base_uri:
        base_uri = add_resources(base_uri, credentials, store)
    
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
        for sync_point in graph.triples((None, TRS.cutoffEvent, None)):
            store.add(sync_point)

    for resource in graph.objects(None, LDP.member): # WTF: en el adaptador de bugzilla es RDFS.member
        response = requests.get(resource.toPython(), auth=credentials, headers={'Accept': 'application/rdf+xml'})
        print(response.content.decode('ascii'))
        store.parse(data=response.content, format='xml')
        store.add((URIRef('_:resourceSet'), URIRef('_:hasResource'), resource))
    
    if (None, LDP.nextPage, RDF.nil) in graph:
        return ''

    else:
        for next_uri in graph.objects(None, LDP.nextPage):
            return next_uri.toPython()


def incremental_update(trs_uri, credentials, store):
    change_log = []
    change_log_uri = trs_uri

    while change_log_uri:
        change_log_uri = find_sync_point(change_log_uri, credentials, store, change_log)
    
    apply_resource_changes(trs_uri, credentials, store, change_log)

    return 1


def find_sync_point(uri, credentials, store, change_log):
    response = requests.get(uri, auth=credentials, headers={'Accept': 'text/turtle'})

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
        if (None, TRS.cutoffEvent, change) in store:
            return ''
        else:
            change_log.insert(0, {"change": change, "resource": resource, "action": action})

    if (None, TRS.previous, RDF.nil) in graph:
        change_log.clear()
        return ''

    else:
        for previous_uri in graph.objects(None, TRS.previous):
            return previous_uri


def apply_resource_changes(uri, credentials, store, change_log):
    for event in change_log:
        if event["action"] == TRS.Creation:
            print("Creating:")
            print(event["resource"])
            response = requests.get(str(event["resource"]), auth=credentials, headers={'Accept': 'application/rdf+xml'})
            print(response.content.decode('ascii'))
            store.parse(data=response.content, format='application/rdf+xml')

            # Send event to EWE Tasker
            evaluate(event['action'], store.triples((event["resource"], None, None)))

            store.add((URIRef('_:resourceSet'), URIRef('_:hasResource'), event["resource"]))

            
        elif event["action"] == TRS.Modification:
            print("Updating:")
            store.remove((event["resource"], None, None))
            response = requests.get(str(event["resource"]), auth=credentials, headers={'Accept': 'application/rdf+xml'})
            print(response.content.decode('ascii'))
            store.parse(data=response.content, format='application/rdf+xml')

            # Send event to EWE Tasker
            evaluate(event['action'], store.triples((event["resource"], None, None)))

            store.add((URIRef('_:resourceSet'), URIRef('_:hasResource'), event["resource"]))


        elif event["action"] == TRS.Deletion:
            print("Deleting:")
            print(event["resource"])

            # Send event to EWE Tasker
            evaluate(event['action'], store.triples((event["resource"], None, None)))

            store.remove((event["resource"], None, None))


        else:
            continue
    
        store.remove((None, TRS.cutoffEvent, None))
        store.add((BNode(), TRS.cutoffEvent, event["change"]))

    return


if __name__ == "__main__":

    # TODO: env variables
    uri = 'http://localhost:8085/OSLC4JBugzilla/services/trs'
    credentials = ('admin', 'adminpass')
    # uri = 'http://localhost:5000/service/trackedResourceSet'
    # credentials = ('', '')
    store = Graph()

    print("\nInitializing...\n")
    initialize(uri, credentials, store)

    print("\nStarting Incremental Update\n")
    while True:
        incremental_update(uri, credentials, store)
        time.sleep(5)

    # print(store.serialize(format='n3', indent=2).decode('ascii'))