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
    "events" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceCreated",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://www.bugzilla.org/rdf#component",
                                  "rdf:value" : "TestComponent"
                                },
                                { "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://purl.org/dc/terms/title",
                                  "rdf:value" : "update"
                                }]
                    }],
    "actions" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/UpdateResource",
                  "rdfs:label": "Update resource",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceURI",
                                  "rdfs:label": "Resource URI", 
                                  "rdf:type": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceURI",
                                  "rdf:value" : "http://172.18.0.1:5000/oslc/rm/requirement/1"
                                },
                                { "@id": "http://example.com/specification_id",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/specification_id",
                                  "rdf:value" : "1"
                                },
                                { "@id": "http://example.com/product",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/product",
                                  "rdf:value" : "OSLC SDK 6"
                                },
                                { "@id": "http://example.com/project",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/project",
                                  "rdf:value" : "OSLC-Project 6"
                                },
                                { "@id": "http://example.com/title",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/title",
                                  "rdf:value" : "OSLC RM Spec 6 - Updated Using EWE"
                                },
                                { "@id": "http://example.com/description",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/description",
                                  "rdf:value" : "The OSLC RM Specification needs to be awesome 6"
                                },
                                { "@id": "http://example.com/source",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/source",
                                  "rdf:value" : "Ian Altman"
                                },
                                { "@id": "http://example.com/author",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/author",
                                  "rdf:value" : "Frank"
                                },
                                { "@id": "http://example.com/category",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/category",
                                  "rdf:value" : "Customer Requirement"
                                },
                                { "@id": "http://example.com/discipline",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/discipline",
                                  "rdf:value" : "Software Development"
                                },
                                { "@id": "http://example.com/revision",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/revision",
                                  "rdf:value" : "0"
                                },
                                { "@id": "http://example.com/target_value",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/target_value",
                                  "rdf:value" : "1"
                                },
                                { "@id": "http://example.com/degree_of_fulfillment",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/degree_of_fulfillment",
                                  "rdf:value" : "0"
                                },
                                { "@id": "http://example.com/status",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/status",
                                  "rdf:value" : "Draft"
                                }]                                
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
                                  "rdf:type" : "http://www.bugzilla.org/rdf#component",
                                  "rdf:value" : "TestComponent"
                                },
                                { "ewe:operation" : "http://www.w3.org/2000/10/swap/string#equalIgnoringCase",
                                  "rdf:type" : "http://purl.org/dc/terms/title",
                                  "rdf:value" : "create"
                                }]
                    }],
    "actions" : [{"@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/CreateResource",
                  "rdfs:label": "Update resource",
                  "rdfs:domain": "http://gsi.dit.upm.es/ontologies/ewe/ns/OSLC",
                  "parameters":[{ "@id": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceURI",
                                  "rdfs:label": "Resource URI", 
                                  "rdf:type": "http://gsi.dit.upm.es/ontologies/ewe/ns/ResourceURI",
                                  "rdf:value" : "http://172.18.0.1:5000/oslc/rm/requirement"
                                },
                                { "@id": "http://example.com/specification_id",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/specification_id",
                                  "rdf:value" : "1"
                                },
                                { "@id": "http://example.com/product",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/product",
                                  "rdf:value" : "OSLC SDK 6"
                                },
                                { "@id": "http://example.com/project",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/project",
                                  "rdf:value" : "OSLC-Project 6"
                                },
                                { "@id": "http://example.com/title",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/title",
                                  "rdf:value" : "OSLC RM Spec 6"
                                },
                                { "@id": "http://example.com/description",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/description",
                                  "rdf:value" : "The OSLC RM Specification needs to be awesome 6"
                                },
                                { "@id": "http://example.com/source",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/source",
                                  "rdf:value" : "Ian Altman"
                                },
                                { "@id": "http://example.com/author",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/author",
                                  "rdf:value" : "Frank"
                                },
                                { "@id": "http://example.com/category",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/category",
                                  "rdf:value" : "Customer Requirement"
                                },
                                { "@id": "http://example.com/discipline",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/discipline",
                                  "rdf:value" : "Software Development"
                                },
                                { "@id": "http://example.com/revision",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/revision",
                                  "rdf:value" : "0"
                                },
                                { "@id": "http://example.com/target_value",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/target_value",
                                  "rdf:value" : "1"
                                },
                                { "@id": "http://example.com/degree_of_fulfillment",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/degree_of_fulfillment",
                                  "rdf:value" : "0"
                                },
                                { "@id": "http://example.com/status",
                                  "rdfs:label": "Resource URI",
                                  "rdf:type": "http://example.com/status",
                                  "rdf:value" : "Draft"
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