#!/bin/sh

set -e

docker run \
    --volume "$PWD"/ansible:/ansible:ro \
    --env ANSIBLE_VAULT_PASSWORD="$ANSIBLE_VAULT_PASSWORD" \
    --tty \
    jcassee/ansible \
    ssh-agent ansible-playbook -e add_ssh_key=yes deploy.yml
