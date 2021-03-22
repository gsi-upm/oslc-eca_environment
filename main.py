from models.roi import Workflow, Step, OSLCServer, Rule
from models.ewetasker import EWETasker
from models.trsclient import TRSClient
from models.activityrecord import EventQueue
from create_workflow import generate_rules, generate_oslc_servers
from visuals import visualize
import time


if __name__ == "__main__":

    ewe_tasker = EWETasker('http://localhost:5050')

    opt = input('\nCreate new workflow? [y/N]: ')

    if opt == 'y':
        # Create a Workflow
        workflow = Workflow()

        n = input('\nNumber of steps for this workflow: ' )
        # Create N Steps
        workflow.create_steps(int(n))

        for step in workflow.steps:
            # Generate OSLC Servers (input and output)
            generate_oslc_servers(step)

            # Import Rules
            generate_rules(step)

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


        queue = EventQueue()
        
        for step in workflow.steps:
            print("\nListening for events\n")
            while True:
                for client in step.clients:
                    client.incremental_update(
                        create_callback = queue.new_create_event,
                        update_callback = queue.new_update_event,
                        delete_callback = queue.new_delete_event
                    )
                    for event in queue.events:
                        queue.events.remove(event)
                        event.add_channel(client.channel)
                        print(step.user.username)
                        print(event.get_rdf())
                        action = ewe_tasker.evaluate(event.get_rdf(), step.user.username)
                        print(action.decode('utf-8'))

                time.sleep(5)


            print('\nStep {}:\n'.format(step.order))
            step.display()
            

    else:
        print('\nExiting...')