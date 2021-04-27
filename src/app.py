from models import Workflow, Step, OSLCServer, Rule
from submodules import EWETasker, TRSClient, EventQueue, ActionQueue, OSLCInterface
from utils import generate_rules, generate_oslc_servers
from visuals import visualize
import time
import yaml

if __name__ == "__main__":

    configfile = input('\nConfig file:')
    with open(configfile, 'r') as stream:
        config = yaml.safe_load(stream)

    ewe_tasker = EWETasker('http://localhost:5050')

    # Create a Workflow
    print('\nCreating workflow {}'.format(config['name']))
    workflow = Workflow(config['name'])

    # Create N Steps
    n = len(config['steps'])
    print('\nCreating {} steps'.format(n))
    workflow.create_steps(int(n))

    for step in workflow.steps:
        # Generate OSLC Servers (input and output)
        generate_oslc_servers(step, config['steps'][step.order-1]['input'], config['steps'][step.order-1]['output'])

        # Import Rules
        print('\nImporting rules')
        generate_rules(step, config['steps'][step.order-1]['rules'])

        # Send Rules to EWE Tasker
        for rule in step.rules:
            ewe_tasker.new_user(step.user)
            ewe_tasker.new_rule(rule)

        # Initializes TRS Client for each input OSLC Server
        for i in step.input:
            trs_client = TRSClient(i.trs, i.user, i.password, i.uri)
            trs_client.initialize()
            trs_client.incremental_update()
            step.clients.append(trs_client)

        print('\nStep {}:\n'.format(step.order))
        step.display()
        input()

    event_queue = EventQueue()
    action_queue = ActionQueue()
    
    while True:

        # Run each step in order
        for step in workflow.steps:

            print("\nListening for events\n")
            while not action_queue.actions:

                # Listen to every input OSLC Server for events
                for client in step.clients:
                    client.incremental_update(
                        create_callback = event_queue.new_create_event,
                        update_callback = event_queue.new_update_event,
                        delete_callback = event_queue.new_delete_event
                    )

                # When there are events, evaluate the rules in EWE Tasker
                for event in event_queue.events:
                    event_queue.events.remove(event)
                    event.add_channel(client.channel)

                    print('\nEvent triggered:\n')
                    print(event.get_rdf())
                    input()

                    actions = ewe_tasker.evaluate(event.get_rdf(), step.user.username)
                    action_queue.add(actions)
                    
                    print('\nActions executed:\n')
                    print(actions.decode('utf-8'))

                time.sleep(5)

            # When EWE Tasker returns an action, execute it
            for action in action_queue.actions:
                action_queue.actions.remove(action)

                oslc_interface = OSLCInterface()
                oslc_interface.set_credentials(step, action)
                oslc_interface.execute(action)
                
                input()