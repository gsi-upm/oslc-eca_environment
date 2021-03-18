import requests

# api = "http://localhost:5050"

class EWETasker:
    def __init__(self, api):
        self.api = api

    def get_rules(self, user):
        url = self.api+"/rules/user/"+str(user)
        return requests.get(url).content

    def new_rule(self, rule):
        url = self.api+"/rules/new"
        payload = rule.rdf.serialize(format='n3')
        requests.post(url, data=payload, headers={'Content-type': 'text/n3'})

    def delete_rule(self, rule):
        url = self.api+"/rules/delete/"+str(rule.uri)
        requests.delete(url)

    def evaluate(self, event):
        url = self.api+"/evaluate"        
        action = requests.post(url, data=event, headers={'Content-type': 'text/n3', 'Accept': 'text/n3'}).content
        return action

    def new_user(self, username, password):
        url = self.api+"/users/new"
        payload = {'username': username,'password':password}
        requests.post(url, data=payload).text

    def delete_user(self, username, password):
        url = self.api+"/users/delete"
        payload = {'username': username,'password': password}
        requests.post(url, data=payload).text