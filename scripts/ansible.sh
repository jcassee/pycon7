#!/bin/sh

set -e

pip install ansible

cd ansible
ansible-playbook deploy.yml
