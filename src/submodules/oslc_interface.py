from rdflib import Namespace, Graph, BNode, RDF
import requests

EWE = Namespace('http://gsi.dit.upm.es/ontologies/ewe/ns/')
OSLC = Namespace('http://open-services.net/ns/core#')
ROI = Namespace('http://gsi.upm.es/ontologies/roi/')
OSLC_CM = Namespace('http://open-services.net/ns/cm#')

class OSLCInterface:
    def set_credentials(self, step, action):
        for output in step.output:
            if output.uri in action.rdf.objects(None, EWE.isProvidedBy):
                self.credentials = (output.user, output.password)

    def execute(self, action):

        for action_type in action.rdf.objects(None, RDF.type):
            if action_type == ROI.CreateResource:
                return self.create(action)

            elif action_type == ROI.UpdateResource:
                return self.update(action)

            elif action_type == ROI.CreDeleteResource:
                return self.delete(action)

        return

    def create(self, action):
        serviceProvider = action.get_service_provider(self.credentials)
        resource = action.get_resource()

        creation_uri = next(uri for uri in serviceProvider.objects(None, OSLC.creation))
        payload = resource.serialize(format='turtle')

        print('\nCreating resource:\n')
        print(payload.decode('utf-8'))

        return requests.post(creation_uri, auth=self.credentials, data=payload, headers={'Content-type': 'text/turtle'})


    def update(self, action):
        serviceProvider = action.__get_service_provider(self.credentials)
        resource = action.get_resource()
        query = action.get_query()

        query_uri = next(uri for uri in serviceProvider.objects(None, OSLC.queryBase))

        data = requests.get(query_uri, auth=self.credentials, headers={'Accept': 'text/n3'}).content
        resource_list = Graph()
        resource_list.parse(format='n3', data=data)

        update_uri = next(result.uri for result in resource_list.query(query))
        payload = resource.serialize(format='turtle')

        print('\nUpdating resource:\n')
        print(payload.decode('utf-8'))

        return requests.put(update_uri, auth=self.credentials, data=payload, headers={'Content-type': 'text/turtle'})


    def delete(self, action):
        serviceProvider = action.get_service_provider(self.credentials)
        query = action.get_query()

        query_uri = next(uri for uri in serviceProvider.objects(None, OSLC.queryBase))

        data = requests.get(query_uri, auth=self.credentials, headers={'Accept': 'text/n3'}).content
        resource_list = Graph()
        resource_list.parse(format='n3', data=data)

        delete_uri = next(result.uri for result in resource_list.query(query))
        print('\nDeleting resource:\n')

        return requests.delete(delete_uri, auth=self.credentials)
