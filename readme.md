# Registro Navale [![Build Status](https://travis-ci.org/jcassee/registronavale.svg)](https://travis-ci.org/jcassee/registronavale)

An example project that demonstrates how to create a hypermedia API using
[Django REST framework](http://www.django-rest-framework.org/) and document it
using Gherkin tests, developed for [PyCon Sette](https://www.pycon.it).
([slides](http://slides.com/jcassee/pycon-sette-hypermedia))

It also demonstrates how to do continuous delivery using Docker and Ansible.
([slides](http://slides.com/jcassee/pycon-sette-deployment))

[**Read the documentation at Relish**](http://www.relishapp.com/jcassee/registronavale)

The [source code](https://github.com/jcassee/registronavale) is available on GitHub.

A [Docker image](https://hub.docker.com/r/jcassee/registronavale) is available on Docker Hub.


## Project layout


### Django

* `registronavale`: The Django project
* `ship_registry`: The ship registry app
* `drf_hal`: HAL-specific functionality


### Docker

The `Dockerfile`, scripts in `scripts` and the files in `config` are used to
build a Docker container to run the Django project.


### Ansible

The `ansible` directory contains an Ansible playbook and roles that deploy the
project to a server. It will deploy both the *master* branch and any GitHub pull
requests.

You need to set `ANSIBLE_VAULT_PASSWORD` to the Ansible Vault password used to
encrypt sensitive information.

    EXPORT ANSIBLE_VAULT_PASSWORD=xxxxxx
    cd ansible
    ansible-playbook deploy.yml


### Gherkin tests and Relish

The project is tested using feature tests written in the Gherkin language. These
can be found in `features`. When deploying the *master* branch, the features are
pushed to Relish where they are rendered as HTML documentation.


### Continuous deployment

The `scripts/integration.sh` script handles the continuous deployment. Although
the project is set up to deploy using Travis CI, it uses Docker containers in
orden to be independent of the CI implementation. Running the deployment scripts
requires the following variables to be set:

* `ANSIBLE_VAULT_PASSWORD`: for decrypting sensitive variables when running the
  Ansible playbook.
* `DOCKER_EMAIL`, `DOCKER_USERNAME` and `DOCKER_PASSWORD`: for pushing the
  Docker image to Docker Hub.
* `RELISH_API_TOKEN`: for pushing the features to Relish.
