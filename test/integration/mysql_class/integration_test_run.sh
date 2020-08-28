#!/bin/bash
# Integration testing program for the module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_class"  
test/integration/mysql_class/fetch_global_var.py
test/integration/mysql_class/fetch_sys_var.py
test/integration/mysql_class/server_init.py
test/integration/mysql_class/server_set_srv_binlog_crc.py
test/integration/mysql_class/server_set_srv_gtid.py
test/integration/mysql_class/server_upd_srv_perf.py

