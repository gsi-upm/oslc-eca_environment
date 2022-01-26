# EWE-OSLC Environment

The scenario can be built using docker-compose:

    docker-compose up -d --build

This builds and runs the docker containers for:

- Bugzilla
- The Bugzilla adapter
- The GitHub adapter
- The OSLC Automation Server

Bugzilla needs to be configured following the instructions in [this tutorial](https://oslc.github.io/developing-oslc-applications/integrating_products_with_oslc/running_the_examples).

EWE Tasker needs to be started as well. In the ewetasker_server directory, run the following command:

    docker-compose up -d --build

Follow the instructions in the [EWE Tasker repo](https://lab.gsi.upm.es/ewe/ewetasker_server.git) for more details on how to configure it.

To interact with the resources and create a workflow that generates an issue when a bug is created, there is a set of requests that can be imported and sent using the [Insomnia](https://docs.insomnia.rest/) tool.