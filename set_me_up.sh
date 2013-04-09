#!/bin/bash
echo "first, create a virtualenv to get a python separated from the system python"
virtualenv .
echo "now use it to bootstrap the buildout..."
bin/python bootstrap.py
echo "run the buildout..."
bin/buildout
echo "run setup. this will pull in many required packages (see requires in setup.py)"
bin/python setup.py develop
