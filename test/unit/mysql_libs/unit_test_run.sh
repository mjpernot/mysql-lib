#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_libs"  
test/unit/mysql_libs/analyze_tbl.py
test/unit/mysql_libs/change_master_to.py
test/unit/mysql_libs/checksum.py
