#!/bin/sh

basedir=`dirname "$0"`
cd "$basedir/../ansible"

sudo add-apt-repository -y ppa:ansible/ansible
sudo apt-get update -q
sudo apt-get install -y ansible

ansible-playbook deploy.yml
