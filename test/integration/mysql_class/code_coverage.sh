#!/bin/bash
# Integration test code coverage for module.
# This will run the Python code coverage module against all integration test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_class test/integration/mysql_class/fetch_global_var.py
coverage run -a --source=mysql_class test/integration/mysql_class/fetch_sys_var.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
