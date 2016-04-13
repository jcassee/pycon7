#!/bin/sh

basedir=`dirname "$0"`
cd "$basedir/../ansible"

ansible-playbook deploy.yml
