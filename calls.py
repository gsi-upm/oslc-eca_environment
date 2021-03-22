import json
import requests
import os
import time
from rdflib import Graph

api = "http://localhost:5050"
# def new_rule(payload):
#     url = api+"/rules/new"
#     data = requests.post(url, json=payload).status_code
#     print(data)

def new_rule():
    url = api+"/rules/new"

    rule = """
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
        @prefix ewe: <http://gsi.dit.upm.es/ontologies/ewe/ns/>.
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.
        @prefix string: <http://www.w3.org/2000/10/swap/string#>.
        @prefix math: <http://www.w3.org/2000/10/swap/math#>.
        {
            ?event1 rdf:type <http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceUpdated>;
                rdf:type ewe:Event;
                ewe:isGeneratedBy <http://gsi.dit.upm.es/ontologies/ewe/ns/OSLCServer>.
            ?event1 ewe:hasParameter ?eparam1.
            ?eparam1 rdf:type <http://open-services.net/ns/core/trs#Modification> .
            ?eparam1 rdf:value ?value .
        } => {
            ewe:action_createresource1 rdf:type <http://gsi.dit.upm.es/ontologies/ewe/ns/CreateResource>; 
                rdf:type ewe:Action;
                ewe:isProvidedBy <http://gsi.dit.upm.es/ontologies/ewe/ns/OSLCServer>.
            ewe:action_createresource1 ewe:hasParameter ewe:resourceuri1.
            ewe:resourceuri1 rdf:type <http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceURI> .
            ewe:resourceuri1  rdf:value ?value . 
        }."""

    payload = """
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> . 
        @prefix ewe: <http://gsi.dit.upm.es/ontologies/ewe/ns/> . 
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . 

        ewe:rule123456789 rdf:type ewe:Rule ;
            rdfs:label "new rule example" ;
            rdfs:comment "New example of a EWE rule" ;
            rdf:value \"""%s\""" ;
            ewe:triggeredBy <http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceCreated> ;
            ewe:executes <http://gsi.dit.upm.es/ontologies/ewe/ns/CreateResource> ;
            ewe:hasCreator <http://gsi.dit.upm.es/ontologies/ewe/ns/usertest> .
    """ % (rule)

    print(payload)

    Graph().parse(data=payload, format='n3')

    data = requests.post(url, data=payload, headers={'Content-type': 'text/n3'}).status_code
    print(data)

def get_rules():
    url = api+"/rules/user/http://gsi.dit.upm.es/ontologies/ewe/ns/usertest"
    data=requests.get(url).text
    data_channels = json.loads(data)
    print(json.dumps(data_channels, indent=2))

def delete_rule(rule_id):
    url = api+"/rules/delete/http://gsi.dit.upm.es/ontologies/ewe/ns/ruletestlabel"+str(rule_id)
    data=requests.delete(url).status_code
    print(data)

def get_channels():
    url = api+"/channels/base"
    data = requests.get(url).text
    data_channels = json.loads(data)
    print(json.dumps(data_channels, indent=2))

def delete_channel():
    url = api+"/channels/custom/delete/http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC"
    data=requests.delete(url).status_code
    print(data)

def new_user(username, password):
    url = api+"/users/new"
    payload = {'username': username,'password':password}
    requests.post(url, data=payload).text

def delete_user(username, password):
    url = api+"/users/delete"
    payload = {'username': username,'password': password}
    requests.post(url, data=payload).text

def evaluate():
    url = api+"/evaluate"
    username = "usertest"
    event = """
        @prefix bugz: <http://www.bugzilla.org/rdf#> .
        @prefix dcterms: <http://purl.org/dc/terms/> .
        @prefix ewe: <http://gsi.dit.upm.es/ontologies/ewe/ns/> .
        @prefix oslc: <http://open-services.net/ns/core#> .
        @prefix oslc_cm: <http://open-services.net/ns/cm#> .
        @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
        @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
        @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

        <http://www.gsi.upm.es/ontologies/roi/event139862529957744> rdf:type <http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceUpdated>;
            rdf:type ewe:Event;
            ewe:isGeneratedBy <http://gsi.dit.upm.es/ontologies/ewe/ns/OSLCServer> ;
            ewe:hasParameter [
                rdf:type <http://open-services.net/ns/core/trs#Modification> ;
                rdf:value "la concha tu mai"
            ] ;
            ewe:hasParameter [
                rdf:type <http://open-services.net/ns/core/trs#Creation> ;
                rdf:value "la concha tu mai"
            ] ;
            ewe:hasParameter [
                rdf:type <http://open-services.net/ns/core/trs#Deletion> ;
                rdf:value "la concha tu mai"
            ] .
    """

    r = requests.post(url, data={"event": event, "username": username})
    print(r.text)
