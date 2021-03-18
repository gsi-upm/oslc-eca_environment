import requests
import os
# TODO: use python packaging system
from actions import actuator

# TODO: env variable
EWE_URL = "http://localhost:5050"
EWE_USER = "usertest"


def evaluate(action, triples):
    url = EWE_URL+"/evaluate"
    payload = """
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix ewe: <http://gsi.dit.upm.es/ontologies/ewe/ns/> .
        @prefix string: <http://www.w3.org/2000/10/swap/string#> .
        @prefix foaf: <http://xmlns.com/foaf/0.1/> .

        _:event rdfs:label "New OSLC resource created" ;
            rdf:type ewe:ResourceCreated ;
            rdf:type ewe:Event ;
            ewe:hasParameter [
                rdf:type {action} ;
                rdf:value "" ;
            ] ;
            rdfs:domain ewe:OSLC .
        
        _:user rdf:type ewe:User ;
            foaf:accountName "{user}" .
    """.format(user=EWE_USER, action=action.n3())

    for (s, p, o) in triples:
        payload += """
        {} {} {} .
        """.format(s.n3(), p.n3(), o.n3())

    print(payload)
    response = requests.post(url, data=payload, headers={'Content-type': 'text/n3', 'Accept': 'text/n3'})
    print("Response from EWE Tasker: "+response.content.decode('utf-8'))

    actuator(response.content)
    return