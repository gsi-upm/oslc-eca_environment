# ROI Integration Environment

Resumen blablabla

## Instructions

Before running the example, the Bugzilla and GitHub services with their respective OSLC and TRS servers have to be running. EWE Tasker also needs initialization.

### Bugzilla

To run a docker container with Bugzilla, follow the Bugzilla Setup section of [this tutorial](https://oslc.github.io/developing-oslc-applications/integrating_products_with_oslc/running_the_examples). The Bugzilla service will be accessible at http://localhost/bugzilla/index.cgi.

To initialize its OSLC and TRS servers, clone the lyo-samples repo:

```bash
git clone https://github.com/OSLC/lyo-samples.git
cd lyo-samples/trs4j-bugzilla-sample
```

Edit the *src/main/resources/bugz.properties* file, enter the credentials you chose for your specific Bugzilla instance in the *admin* and *admin_password* properties. Run the OSLC-TRS server (you need to have [Java](https://java.com/en/download/help/download_options.html) and [Maven](http://maven.apache.org/install.html) installed):

```bash
mvn clean jetty:run
```

Access the service at http://localhost:8085/OSLC4JBugzilla/services/trs/base and check if it works.

The OSLC Bugzilla service can give permission problems when trying to make POST and PUT requests directly. In that case, [this](https://lab.gsi.upm.es/smartdevops/bugzilla-oslc_adapter) alternative OSLC adapter can be used. Clone the repo and start it:

```bash
git clone https://lab.gsi.upm.es/smartdevops/bugzilla-oslc_adapter.git
cd bugzilla-oslc_adapter
```

Create a *.env* file and asign the *BUGZILLA_URL* and *BUGZILLA_API_KEY* variables. You can set up your API key inside Bugzilla by using the *API Keys* tab in the *Preferences* pages.

```bash
docker-compose up
```

Go to http://localhost:5000/service/serviceProviders/catalog to check if it's working.

This adapter doesn't have TRS capabilities so **it needs to be used with the other one at the same time**. 

#### Troubleshooting

If problems are encountered running the TRS server from the lyo-samples repo, check [this tutorial](http://wiki.eclipse.org/Lyo/BuildTRS4JBugzilla).

### GitHub

Get the OSLC and TRS adapter for GitHub:

```bash
git clone https://lab.gsi.upm.es/smartdevops/github-oslc_adapter.git
cd bugzilla-oslc_adapter
```

Create a *.env* file and asign the *GITHUB_TOKEN* variable. In your GitHub profile, go to *Settings* > *Developer Settings* > *Personal access tokens* to get the token.

```bash
docker-compose up
```

You also need to configure a webhook to send POST requests to your adapter whenever a change occurs to an issue. In your repository, go to *Settings* > *Webhooks* and enter you URL. Your adapter must be accessible from the Internet.

### EWE Tasker

Go to https://lab.gsi.upm.es/ewe/ewetasker_server.git and follow the documentation to start up the EWE Tasker server.

### ROI

Clone this repository and run it with ```docker-compose up --build```.