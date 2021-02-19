import requests
import rdflib
import time
import json

def fetchChanges(uri):

    # The URI for the data you want to fetch
    #uri = uri

    # The content type you want to set in the Request Headers.
    # This example is for RDF/XML
    headers = {'Accept': 'application/rdf+xml'}

    # Credentials
    user = r'admin'
    password = r'adminpass'

    # Build the request with the URI and Header parameters
    return requests.get(uri, auth=(user, password), headers=headers)


def getChangeLog(response):

    # Create an empty graph that we can load data into
    graph = rdflib.Graph()

    # Parse the fetched data into the graph and tell the code that the
    graph.parse(data=response.content)

    # SPARQL query
    return graph.query("""

                         select ?changed ?order

                         where {
                            ?s <http://open-services.net/ns/core/trs#changed> ?changed .
                            ?s <http://open-services.net/ns/core/trs#order> ?order .
                         }

                         order by ?order

                         """)


def trigger_event(graph):
    url = "http://localhost:5050/evaluate"
    payload = {
        "username": "usertest",
        "event": """
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix ewe: <http://gsi.dit.upm.es/ontologies/ewe/ns/> .
        @prefix string: <http://www.w3.org/2000/10/swap/string#> .

        _:event rdfs:label "New OSLC resource created" ;
            rdf:type ewe:ResourceCreated ;
            rdf:type ewe:Event ;"""
    }

    for pred, obj in graph.predicate_objects():
        print(pred, ": ", obj)
        payload["event"] = payload["event"] + """
            ewe:hasParameter [
                rdf:type <{}> ;
                rdf:value "{}" ;
            ] ;""".format(pred, obj)
        
    payload["event"] = payload["event"] + """
            rdfs:domain ewe:OSLC .
    """
    
    print(payload["event"])
    graph.parse(data=payload["event"], format='n3')
    r = requests.post(url, data=payload)
    print(r.text)


response = fetchChanges('http://localhost:8085/OSLC4JBugzilla/services/trs')
previous = getChangeLog(response)
max = int(list(previous)[-1][1])

print('Listening for changes\n')

while True:
    # print('Polling...\n')

    time.sleep(2)

    response = fetchChanges('http://localhost:8085/OSLC4JBugzilla/services/trs')
    changes = getChangeLog(response)

    if changes != previous:
        previous = changes

        # For each results print the value
        for row in changes:
            if int(row[1]) > max:
                max = int(row[1])

                response = fetchChanges(row[0])

                graph = rdflib.Graph()
                graph.parse(data=response.content)

                data = graph.serialize(format='n3', indent=2)
                print(row[0])
                print('\n')
                print(data.decode('ascii'))

                trigger_event(graph)
