#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_libs"  
/usr/bin/python3 ./test/unit/mysql_libs/_io_wait_chk.py
/usr/bin/python3 ./test/unit/mysql_libs/_sql_wait_chk.py
/usr/bin/python3 ./test/unit/mysql_libs/analyze_tbl.py
/usr/bin/python3 ./test/unit/mysql_libs/change_master_to.py
/usr/bin/python3 ./test/unit/mysql_libs/checksum.py
/usr/bin/python3 ./test/unit/mysql_libs/check_tbl.py
/usr/bin/python3 ./test/unit/mysql_libs/chg_slv_state.py
/usr/bin/python3 ./test/unit/mysql_libs/create_instance.py
/usr/bin/python3 ./test/unit/mysql_libs/disconnect.py
/usr/bin/python3 ./test/unit/mysql_libs/fetch_db_dict.py
/usr/bin/python3 ./test/unit/mysql_libs/fetch_logs.py
/usr/bin/python3 ./test/unit/mysql_libs/fetch_tbl_dict.py
/usr/bin/python3 ./test/unit/mysql_libs/optimize_tbl.py
/usr/bin/python3 ./test/unit/mysql_libs/purge_bin_logs.py
/usr/bin/python3 ./test/unit/mysql_libs/reset_master.py
/usr/bin/python3 ./test/unit/mysql_libs/reset_slave.py
/usr/bin/python3 ./test/unit/mysql_libs/select_wait_until.py
/usr/bin/python3 ./test/unit/mysql_libs/create_slv_array.py
/usr/bin/python3 ./test/unit/mysql_libs/crt_cmd.py
/usr/bin/python3 ./test/unit/mysql_libs/fetch_slv.py
/usr/bin/python3 ./test/unit/mysql_libs/find_name.py
/usr/bin/python3 ./test/unit/mysql_libs/is_cfg_valid.py
/usr/bin/python3 ./test/unit/mysql_libs/is_logs_synced.py
/usr/bin/python3 ./test/unit/mysql_libs/is_rep_delay.py
/usr/bin/python3 ./test/unit/mysql_libs/start_slave_until.py
/usr/bin/python3 ./test/unit/mysql_libs/switch_to_master.py
/usr/bin/python3 ./test/unit/mysql_libs/sync_delay.py
/usr/bin/python3 ./test/unit/mysql_libs/sync_rep_slv.py
/usr/bin/python3 ./test/unit/mysql_libs/wait_until.py

