#!/bin/bash
# Integration testing program for the module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_class"  
/usr/bin/python ./test/integration/mysql_class/fetch_global_var.py
/usr/bin/python ./test/integration/mysql_class/fetch_sys_var.py
/usr/bin/python ./test/integration/mysql_class/server_chg_db.py
/usr/bin/python ./test/integration/mysql_class/server_cmd_sql.py
/usr/bin/python ./test/integration/mysql_class/server_col_sql.py
/usr/bin/python ./test/integration/mysql_class/server_connect.py
/usr/bin/python ./test/integration/mysql_class/server_disconnect.py
/usr/bin/python ./test/integration/mysql_class/server_get_name.py
/usr/bin/python ./test/integration/mysql_class/server_init.py
/usr/bin/python ./test/integration/mysql_class/server_is_connected.py
/usr/bin/python ./test/integration/mysql_class/server_reconnect.py
/usr/bin/python ./test/integration/mysql_class/server_set_pass_config.py
/usr/bin/python ./test/integration/mysql_class/server_set_srv_binlog_crc.py
/usr/bin/python ./test/integration/mysql_class/server_set_srv_gtid.py
/usr/bin/python ./test/integration/mysql_class/server_setup_ssl.py
/usr/bin/python ./test/integration/mysql_class/server_sql.py
/usr/bin/python ./test/integration/mysql_class/server_upd_srv_perf.py
/usr/bin/python ./test/integration/mysql_class/server_upd_srv_stat.py
/usr/bin/python ./test/integration/mysql_class/server_vert_sql.py

