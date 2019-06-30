#!/bin/bash
# Unit test code coverage for module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mysql_class test/unit/mysql_class/fetch_global_var.py
coverage run -a --source=mysql_class test/unit/mysql_class/fetch_sys_var.py
coverage run -a --source=mysql_class test/unit/mysql_class/flush_logs.py
coverage run -a --source=mysql_class test/unit/mysql_class/show_master_stat.py
coverage run -a --source=mysql_class test/unit/mysql_class/show_slave_hosts.py
coverage run -a --source=mysql_class test/unit/mysql_class/show_slave_stat.py
coverage run -a --source=mysql_class test/unit/mysql_class/slave_start.py
coverage run -a --source=mysql_class test/unit/mysql_class/slave_stop.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_str.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_union.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_eq.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_ge.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_gt.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_le.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_lt.py
coverage run -a --source=mysql_class test/unit/mysql_class/GTIDSet_ne.py
coverage run -a --source=mysql_class test/unit/mysql_class/Position_cmp.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_setsrvbinlogcrc.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
