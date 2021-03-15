import json
import requests
import os
import time

api = "http://localhost:5050"
def new_rule(payload):
    url = api+"/rules/new"
    data = requests.post(url, json=payload).status_code
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
                rdf:type <http://open-services.net/ns/core/trs#Creation> ;
                rdf:value "" ;
            ] ;
            rdfs:domain ewe:OSLC .
        
        _:user rdf:type ewe:User ;
            foaf:accountName "usertest" .
    
        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://purl.org/dc/terms/description> "ejemplo" .

        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://open-services.net/ns/cm#status> "open" .
        
        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://open-services.net/ns/cm#ChangeRequest> .
        
        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://purl.org/dc/terms/modified> "2021-03-15T16:23:55"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
        
        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://purl.org/dc/terms/contributor> "None" .
        
        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://purl.org/dc/terms/title> "ejemplo" .
        
        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://purl.org/dc/terms/created> "2021-03-15T16:23:55"^^<http://www.w3.org/2001/XMLSchema#dateTime> .
        
        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://open-services.net/ns/core#serviceProvider> <http://localhost:5000/service/serviceProviders/345978727> .
        
        <http://localhost:5000/service/serviceProviders/345978727/changeRequests/88> <http://purl.org/dc/terms/identifier> "88"^^<http://www.w3.org/2001/XMLSchema#integer> .
    """

    r = requests.post(url, data=payload, headers={'Content-type': 'text/n3', 'Accept': 'text/n3'})
    print(r.text)
