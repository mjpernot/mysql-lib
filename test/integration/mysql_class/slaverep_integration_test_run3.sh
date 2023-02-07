#!/bin/bash
# Integration testing program for the module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_class"  
/usr/bin/python3 ./test/integration/mysql_class/fetch_global_var.py
/usr/bin/python3 ./test/integration/mysql_class/fetch_sys_var.py
/usr/bin/python3 ./test/integration/mysql_class/flush_logs.py
/usr/bin/python3 ./test/integration/mysql_class/gtidset.py
/usr/bin/python3 ./test/integration/mysql_class/masterrep_connect.py
/usr/bin/python3 ./test/integration/mysql_class/masterrep_init.py
/usr/bin/python3 ./test/integration/mysql_class/masterrep_get_log_info.py
/usr/bin/python3 ./test/integration/mysql_class/masterrep_show_slv_hosts.py
/usr/bin/python3 ./test/integration/mysql_class/masterrep_upd_mst_status.py
/usr/bin/python3 ./test/integration/mysql_class/rep_fetch_do_db.py
/usr/bin/python3 ./test/integration/mysql_class/rep_fetch_ign_db.py
/usr/bin/python3 ./test/integration/mysql_class/rep_get_serv_id.py
/usr/bin/python3 ./test/integration/mysql_class/rep_init.py
/usr/bin/python3 ./test/integration/mysql_class/server_chg_db.py
/usr/bin/python3 ./test/integration/mysql_class/server_cmd_sql.py
/usr/bin/python3 ./test/integration/mysql_class/server_col_sql.py
/usr/bin/python3 ./test/integration/mysql_class/server_connect.py
/usr/bin/python3 ./test/integration/mysql_class/server_disconnect.py
/usr/bin/python3 ./test/integration/mysql_class/server_fetch_log.py
/usr/bin/python3 ./test/integration/mysql_class/server_fetch_mst_rep_cfg.py
/usr/bin/python3 ./test/integration/mysql_class/server_fetch_slv_rep_cfg.py
/usr/bin/python3 ./test/integration/mysql_class/server_flush_logs.py
/usr/bin/python3 ./test/integration/mysql_class/server_get_name.py
/usr/bin/python3 ./test/integration/mysql_class/server_init.py
/usr/bin/python3 ./test/integration/mysql_class/server_is_connected.py
/usr/bin/python3 ./test/integration/mysql_class/server_reconnect.py
/usr/bin/python3 ./test/integration/mysql_class/server_set_srv_binlog_crc.py
/usr/bin/python3 ./test/integration/mysql_class/server_set_srv_gtid.py
/usr/bin/python3 ./test/integration/mysql_class/server_sql.py
/usr/bin/python3 ./test/integration/mysql_class/server_upd_log_stats.py
/usr/bin/python3 ./test/integration/mysql_class/server_upd_mst_rep_stat.py
/usr/bin/python3 ./test/integration/mysql_class/server_upd_slv_rep_stat.py
/usr/bin/python3 ./test/integration/mysql_class/server_upd_srv_perf.py
/usr/bin/python3 ./test/integration/mysql_class/server_upd_srv_stat.py
/usr/bin/python3 ./test/integration/mysql_class/server_vert_sql.py
/usr/bin/python3 ./test/integration/mysql_class/show_master_stat.py
/usr/bin/python3 ./test/integration/mysql_class/show_slave_hosts.py
/usr/bin/python3 ./test/integration/mysql_class/show_slave_stat.py
/usr/bin/python3 ./test/integration/mysql_class/slave_start.py
/usr/bin/python3 ./test/integration/mysql_class/slave_stop.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_connect.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_fetch_do_tbl.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_fetch_ign_tbl.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_get_err_stat.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_get_log_info.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_get_others.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_get_thr_stat.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_get_time.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_init.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_is_slave_up.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_is_slv_error.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_is_slv_running.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_show_slv_state.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_start_slave.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_stop_slave.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_upd_gtid_pos.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_upd_slv_state.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_upd_slv_status.py
/usr/bin/python3 ./test/integration/mysql_class/slaverep_upd_slv_time.py

