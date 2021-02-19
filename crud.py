import requests
from rdflib import Graph, term
import json
import datetime


# PYOSLC
def updateResource():
  uri = "http://localhost:5000/oslc/rm/requirement/X1C2V3B1"

  payload = {
    "specification_id": "X1C2V3B6",
    "product": "OSLC SDK 6",
    "project": "OSLC-Project 6",
    "title": "OSLC RM Spec 6 - OK",
    "description": "The OSLC RM Specification needs to be awesome 6",
    "source": "Ian Altman",
    "author": "Frank",
    "category": "Customer Requirement",
    "discipline": "Software Development",
    "revision": "0",
    "target_value": "1",
    "degree_of_fulfillment": "0",
    "status": "Draft"
  }

  headers = {
    'Accept': 'application/json',
    'Content-type': 'application/json'
  }

  r = requests.put(uri, json=payload, headers=headers)
  print(r.status_code)


# BUGZILLA

# headers = {'Accept': 'application/rdf+xml'}

# user = r'admin'
# password = r'adminpass'

# uri = 'http://localhost:8085/OSLC4JBugzilla/services/resourceShapes/changeRequest'
# r = requests.get(uri, auth=(user, password), headers=headers)

# print(r.text)

# graph = Graph()
# graph.parse(format='xml', data=r.text)
# resourceShape = graph.query("""

#   prefix oslc: <http://open-services.net/ns/core#>

#   select ?property ?name

#   where {
#     ?s oslc:propertyDefinition ?property .
#     ?s oslc:name ?name .
#   }

# """)

# properties = {}
# for row in resourceShape:
#   properties[row[0].toPython()] = row[1].toPython()

# print(properties)


# uri = 'http://localhost:8085/OSLC4JBugzilla/services/1/changeRequests/49'
# r = requests.get(uri, auth=(user, password), headers=headers)

# graph = Graph()
# graph.parse(format='xml', data=r.text)

# payload = {}
# for pred, obj in graph.predicate_objects():
#   if pred.toPython() in properties.keys():
#     if type(obj.toPython()) == datetime.datetime:
#       payload[properties[pred.toPython()]] = obj.toPython().strftime("%Y-%m-%d %H:%M:%S")
#     else:
#       payload[properties[pred.toPython()]] = obj.toPython()
    
# payload['title'] = 'hola'
# print(payload)

# headers = {
#   'Accept': 'application/json',
#   'Content-type': 'application/json'
# }
# r = requests.put(uri, auth=(user, password), json=payload, headers=headers)
# print(r.status_code)

def createResource():
  headers = {'Content-type': 'application/rdf+xml'}

  user = r'bugs@localhost.here'
  password = r'bugs4me'

  uri = 'http://ermo-debian:8080/OSLC4JBugzilla/services/1/changeRequests/1'

  r = requests.get(uri, auth=(user, password), headers=headers)
  print(r.status_code)

  uri = 'http://ermo-debian:8080/OSLC4JBugzilla/services/1/changeRequests'

  payload = """<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF
        xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        xmlns:oslc="http://open-services.net/ns/core#"
        xmlns:bugz="http://www.bugzilla.org/rdf#"
        xmlns:foaf="http://xmlns.com/foaf/0.1/"
        xmlns:dcterms="http://purl.org/dc/terms/"
        xmlns:oslc_cm="http://open-services.net/ns/cm#">
      <oslc_cm:ChangeRequest>
        <bugz:operatingSystem>Linux</bugz:operatingSystem>
        <rdf:type rdf:resource="http://open-services.net/ns/cm#ChangeRequest"/>
        <oslc_cm:status>NEW</oslc_cm:status>
        <bugz:priority>---</bugz:priority>
        <dcterms:title>New bug entered from OSLC Adapter</dcterms:title>
        <bugz:version>unspecified</bugz:version>
        <bugz:platform>PC</bugz:platform>
        <dcterms:contributor>
          <foaf:Person rdf:about="http://localhost:8085/OSLC4JBugzilla/person?mbox=admin">
            <foaf:mbox>admin</foaf:mbox>
          </foaf:Person>
        </dcterms:contributor>
        <bugz:component>Server</bugz:component>
        <oslc_cm:severity>Unclassified</oslc_cm:severity>
      </oslc_cm:ChangeRequest>
    </rdf:RDF>"""

  r = requests.post(uri, auth=(user, password), data=payload, headers=headers)
  print(r.status_code)

  return

def getShape(serviceProvider):
  headers = {'Accept': 'application/rdf+xml'}

  user = r'admin'
  password = r'adminpass'

  r = requests.get(serviceProvider, auth=(user, password), headers=headers)

  graph = Graph()
  graph.parse(format="xml", data=r.text)
  resourceShape = graph.query("""

    prefix oslc: <http://open-services.net/ns/core#>

    select ?shape

    where {
      ?s oslc:creationFactory ?o .
      ?o oslc:resourceShape ?shape .
    }

  """)
  return resourceShape