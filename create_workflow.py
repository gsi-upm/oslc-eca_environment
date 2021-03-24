from models.roi import Workflow, Step, OSLCServer, Rule
from tkinter import filedialog
from rdflib import Graph


def generate_oslc_servers(step):
    print('\nChoose OSLC servers to get input from:')
    # oslc_server = new_oslc_server()
    oslc_server = OSLCServer(
        name = 'Github', 
        oslc = 'http://localhost:5001/service/catalog',
        trs = 'http://localhost:5001/service/trackedResourceSet',
        user = '',
        password = ''
    )

    print('\n  - {} OSLC server:\n'.format(oslc_server.name))
    oslc_server.display()
    step.add_input(oslc_server)
    input()


    print('\nChoose OSLC servers to get output from:')
    # oslc_server = new_oslc_server()
    oslc_server = OSLCServer(
        name = 'Bugzilla', 
        oslc = 'http://localhost:5000/service/serviceProviders/catalog',
        trs = 'http://localhost:8085/OSLC4JBugzilla/services/trs',
        user = 'admin',
        password = 'adminpass'
    )

    print('\n  - {} OSLC server:\n'.format(oslc_server.name))
    oslc_server.display()
    step.add_output(oslc_server)
    input()


def generate_rules(step):
    print('\nChoose rules from file:\n')
    rule = Rule(step.user)
    # new_rule(rule)
    # with open('rules/bug_issue_create.n3') as reader:
    with open('rules/issue_bug_create.n3') as reader:
        rule.set_value(reader.read())

    print('\nImported rule:\n')
    g = Graph()
    g.parse(data=rule.value, format='n3')
    print(g.serialize(format='n3').decode('utf-8'))
    step.add_rule(rule)
    input()

    print('\nChoose rules from file:\n')
    rule = Rule(step.user)
    # new_rule(rule)
    # with open('rules/bug_issue_update.n3') as reader:
    with open('rules/issue_bug_update.n3') as reader:
        rule.set_value(reader.read())

    print('\nImported rule:\n')
    print(rule.value)
    step.add_rule(rule)
    input()


def new_oslc_server():
    name = input('\n  - Enter a name for the OSLC Server: ')
    oslc = input('\n  - Provide URI of the OSLC ServiceProvider: ')
    trs = input('\n  - Provide URI of the TRS: ')
    user = input('\n  - Enter user: ')
    password = input('\n  - Enter password: ')

    return OSLCServer(name, oslc, trs, user, password)


def new_rule(rule):
    file_path = filedialog.askopenfilename()
    with open(file_path) as reader:
        rule.set_value(reader.read())

    return