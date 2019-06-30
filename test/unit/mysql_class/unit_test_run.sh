#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_class"  
test/unit/mysql_class/fetch_global_var.py
test/unit/mysql_class/fetch_sys_var.py
test/unit/mysql_class/flush_logs.py
test/unit/mysql_class/show_master_stat.py
test/unit/mysql_class/show_slave_hosts.py
test/unit/mysql_class/show_slave_stat.py
test/unit/mysql_class/slave_start.py
test/unit/mysql_class/slave_stop.py
test/unit/mysql_class/GTIDSet_init.py
test/unit/mysql_class/GTIDSet_str.py
test/unit/mysql_class/GTIDSet_union.py
test/unit/mysql_class/GTIDSet_eq.py
test/unit/mysql_class/GTIDSet_ge.py
test/unit/mysql_class/GTIDSet_gt.py
test/unit/mysql_class/GTIDSet_le.py
test/unit/mysql_class/GTIDSet_lt.py
test/unit/mysql_class/GTIDSet_ne.py
test/unit/mysql_class/Position_cmp.py
test/unit/mysql_class/Server_init.py
test/unit/mysql_class/Server_setsrvbinlogcrc.py
test/unit/mysql_class/Server_setsrvgtid.py

