#!/bin/bash
echo "first, create a virtualenv to get a python separated from the system python"
echo "if your virtualenv command is named differently, change it here:"
echo "the --no-site-packages parameter is optional or not needed in versions where that was fixed anyways. it will do no harm..."
virtualenv --no-site-packages .
echo "now use it to bootstrap the buildout..."
bin/python bootstrap.py
echo "run the buildout..."
bin/buildout
echo "run setup. this will pull in many required packages (see requires in setup.py)"
bin/python setup.py develop
echo "make the app serve with settings from development.ini (port 8080, change if needed)"
bin/pserve development.ini
