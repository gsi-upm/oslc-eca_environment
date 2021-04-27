from models.roi import Workflow, Step, OSLCServer, Rule
from tkinter import filedialog
from rdflib import Graph


def generate_oslc_servers(step, inputs, outputs):
    for i in inputs:
        oslc_server = OSLCServer(
            name = i['name'], 
            oslc = i['oslc'],
            trs = i['trs'],
            user = i['user'],
            password = i['password']
        )

        print('\nConnecting to {} OSLC server:\n'.format(oslc_server.name))
        oslc_server.display()
        step.add_input(oslc_server)
        input()


    for o in outputs:
        oslc_server = OSLCServer(
            name = o['name'], 
            oslc = o['oslc'],
            trs = o['trs'],
            user = o['user'],
            password = o['password']
        )

        print('\nConnecting to {} OSLC server:\n'.format(oslc_server.name))
        oslc_server.display()
        step.add_output(oslc_server)
        input()


def generate_rules(step, rules):
    for file in rules:
        rule = Rule(step.user)

        with open('rules/'+file) as reader:
            rule.set_value(reader.read())

        print('\nNew rule:\n')
        g = Graph()
        g.parse(data=rule.value, format='n3')
        print(g.serialize(format='n3').decode('utf-8'))
        step.add_rule(rule)
        input()