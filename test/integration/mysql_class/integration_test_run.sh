#!/bin/bash
# Integration testing program for the module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_class"  
test/integration/mysql_class/fetch_global_var.py
test/integration/mysql_class/fetch_sys_var.py

