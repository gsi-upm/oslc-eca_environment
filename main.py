from models.roi import Workflow, Step, OSLCServer, Rule
from create_workflow import generate_rules, generate_oslc_servers
from visuals import visualize


if __name__ == "__main__":

    opt = input('\nCreate new workflow? [y/N]: ')

    if opt == 'y':
        workflow = Workflow()

        n = input('\nNumber of steps for this workflow: ' )
        workflow.create_steps(int(n))

        for step in workflow.steps:
            generate_oslc_servers(step)
            generate_rules(step)

            print('\nStep {}:\n'.format(step.order))
            step.display()
            

    else:
        print('\nExiting...')