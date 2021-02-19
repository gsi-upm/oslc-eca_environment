import requests

import rdflib
# import rdflib_jsonld

# The URI for the data you want to fetch

uri = 'http://localhost:8085/OSLC4JBugzilla/services/trs'

# The content type you want to set in the Request Headers.

# This example is for RDF/XML

headers = {'Accept': 'application/rdf+xml'}

# Credentials

user = r'admin'
password = r'estapaladmin'

# Build the request with the URI and Header parameters

response = requests.get(uri, auth=(user, password), headers=headers)

# Fetch the request

# response = url.urlopen(request)

# Read and Print the request

# data = response.read()
data = response.text

print(data)
print('\n\n')

# Start of Parsing Data Code Example

# Create an empty graph that we can load data into

graph = rdflib.Graph()

# Parse the fetched data into the graph and tell the code that the

#format of the data is N-triple ('xml')

graph.parse(data=response.content)

# To make sure it worked we will serialize the data at N-triples

#('nt') and print it out

# The response should be the same as the data that we initially parsed

#into the graph (order of the triples does not matter)

data = graph.serialize(format='turtle')

print(data.decode('ascii'))

# Form the SPARQL query

# Grab a list of all of the Predicates in the graph

# predicates = graph.predicates(subject=None, object=None)
#
# # For each item in the predicates generator, print it out
#
# for predicate in predicates:
#
#     print(predicate)

#
print('\n\nPRDICATES\n')
predicates = graph.predicates(object=None, subject=None)

for p in predicates:

    print(p)

print('\n\nSUBJECTS\n')
subjects = graph.subjects(object=None, predicate=None)

for s in subjects:

    print(s)

print('\n\nOBJECTS\n')
objects = graph.objects(predicate=None, subject=None)

for o in objects:

    print(o)
# Form the SPARQL query
#
# predicate_query = graph.query("""
#
#                      select ?objects
#
#                      where {?s <http://open-services.net/ns/core/trs#change> ?objects}
#
#                      """)
#
# # For each results print the value
#
# for row in predicate_query:
#
#     print('%s' % row)
