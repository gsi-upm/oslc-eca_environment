import requests

class EWETasker:
    def __init__(self, api):
        self.api = api

    def get_rules(self, user):
        url = self.api+"/rules/user/"+str(user.uri)
        return requests.get(url).content

    def new_rule(self, rule):
        url = self.api+"/rules/new"
        payload = rule.rdf.serialize(format='n3')
        requests.post(url, data=payload, headers={'Content-type': 'text/n3'})

    def delete_rule(self, rule):
        url = self.api+"/rules/delete/"+str(rule.uri)
        requests.delete(url)

    def evaluate(self, event, username):
        url = self.api+"/evaluate"
        payload = {"username": username, "event": event}
        action = requests.post(url, data=payload, headers={'Accept': 'text/n3'}).content
        return action

    def new_user(self, user):
        url = self.api+"/users/new"
        payload = {'username': user.username, 'password': user.password}
        requests.post(url, data=payload).text

    def delete_user(self, user):
        url = self.api+"/users/delete"
        payload = {'username': user.username, 'password': user.password}
        requests.post(url, data=payload).text