query_rule = {
    "@context" : {
        "@vocab" : "http://gsi.dit.upm.es/ontologies/ewe/ns/"
        },
    "rdfs:label" : 'Resource created',
    "rdfs:comment" : 'A resource was created',
    "ewe:hasCreator" : 'http://gsi.dit.upm.es/ontologies/ewe/ns/usertest',
    "events" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceCreated",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://www.bugzilla.org/rdf#component",
                                  "rdf:value" : "TestComponent"
                                }]
                    }],
    "actions" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/QueryResource",
                  "rdfs:label": "Query resource",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/QueryURI",
                                  "rdfs:label": "Query URI", 
                                  "rdf:type": "http://gsi.dit.upm.es/ontologies/ewe/ns/QueryURI",
                                  "rdf:value" : "http://localhost:8085/OSLC4JBugzilla/services/1/changeRequests"
                                }]                                
                    }]
    }

chain_rule = {
    "@context" : {
        "@vocab" : "http://gsi.dit.upm.es/ontologies/ewe/ns/"
        },
    "rdfs:label" : 'Resource created',
    "rdfs:comment" : 'A resource was created',
    "ewe:hasCreator" : 'http://gsi.dit.upm.es/ontologies/ewe/ns/usertest',
    "events" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceCreated",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://www.bugzilla.org/rdf#component",
                                  "rdf:value" : "TestComponent"
                                }]
                    }],
    "actions" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/QueryResource",
                  "rdfs:label": "Query resource",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/QueryURI",
                                  "rdfs:label": "Query URI", 
                                  "rdf:type": "http://gsi.dit.upm.es/ontologies/ewe/ns/QueryURI",
                                  "rdf:value" : "http://localhost:5000/oslc/rm/requirement"
                                },
                                { "@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/EventInput",
                                  "rdfs:label": "Event Input", 
                                  "rdf:type": "http://gsi.dit.upm.es/ontologies/ewe/ns/EventInput",
                                  "rdf:value" : "true"
                                }]                                
                  },
                  {"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/UpdateResource",
                "rdfs:label": "Update resource",
                "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                "parameters":[{ "@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/PreviousOutput",
                                "rdfs:label": "Previous Output", 
                                "rdf:type": "http://gsi.dit.upm.es/ontologies/ewe/ns/PreviousOutput",
                                "rdf:value" : "true"
                              }]                                
                  }]
    }

update_rule = {
    "@context" : {
        "@vocab" : "http://gsi.dit.upm.es/ontologies/ewe/ns/"
        },
    "rdfs:label" : 'Resource created',
    "rdfs:comment" : 'A resource was created',
    "ewe:hasCreator" : 'http://gsi.dit.upm.es/ontologies/ewe/ns/usertest',
    "events" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceUpdated",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://open-services.net/ns/core/trs#Modification",
                                  "rdf:value" : ""
                                }]
                    }],
    "actions" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/UpdateResource",
                  "rdfs:label": "Update resource",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[]                                
                    }]
    }

create_rule = {
    "@context" : {
        "@vocab" : "http://gsi.dit.upm.es/ontologies/ewe/ns/"
        },
    "rdfs:label" : 'Resource created',
    "rdfs:comment" : 'A resource was created',
    "ewe:hasCreator" : 'http://gsi.dit.upm.es/ontologies/ewe/ns/usertest',
    "events" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceCreated",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://open-services.net/ns/core/trs#Creation",
                                  "rdf:value" : ""
                                }]
                    }],
    "actions" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/CreateResource",
                  "rdfs:label": "Create resource",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/CreationURI",
                                  "rdfs:label": "Resource URI", 
                                  "rdf:type": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceURI",
                                  "rdf:value" : "http://localhost:5000/service/serviceProviders/345978727/changeRequests"
                                }]                  
                    }]
    }


delete_rule = {
    "@context" : {
        "@vocab" : "http://gsi.dit.upm.es/ontologies/ewe/ns/"
        },
    "rdfs:label" : 'Resource created',
    "rdfs:comment" : 'A resource was created',
    "ewe:hasCreator" : 'http://gsi.dit.upm.es/ontologies/ewe/ns/usertest',
    "events" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceCreated",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://www.bugzilla.org/rdf#component",
                                  "rdf:value" : "TestComponent"
                                },
                                { "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://purl.org/dc/terms/title",
                                  "rdf:value" : "delete"
                                }]
                    }],
    "actions" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/DeleteResource",
                  "rdfs:label": "Update resource",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceURI",
                                  "rdfs:label": "Resource URI", 
                                  "rdf:type": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceURI",
                                  "rdf:value" : "http://172.18.0.1:5000/oslc/rm/requirement/1"
                                }]                                
                    }]
    }