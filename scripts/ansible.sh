#!/bin/sh

set -e

sudo add-apt-repository -y ppa:ansible/ansible
sudo apt-get update -q
sudo apt-get install -y ansible

cd ansible
ansible-playbook deploy.yml
