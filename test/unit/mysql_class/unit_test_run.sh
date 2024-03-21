#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo "Unit test: mysql_class"  
/usr/bin/python ./test/unit/mysql_class/fetch_global_var.py
/usr/bin/python ./test/unit/mysql_class/fetch_sys_var.py
/usr/bin/python ./test/unit/mysql_class/flush_logs.py
/usr/bin/python ./test/unit/mysql_class/show_master_stat.py
/usr/bin/python ./test/unit/mysql_class/show_slave_hosts.py
/usr/bin/python ./test/unit/mysql_class/show_slave_stat.py
/usr/bin/python ./test/unit/mysql_class/slave_start.py
/usr/bin/python ./test/unit/mysql_class/slave_stop.py
/usr/bin/python ./test/unit/mysql_class/gtidset_or.py
/usr/bin/python ./test/unit/mysql_class/gtidset_init.py
/usr/bin/python ./test/unit/mysql_class/gtidset_str.py
/usr/bin/python ./test/unit/mysql_class/gtidset_union.py
/usr/bin/python ./test/unit/mysql_class/gtidset_eq.py
/usr/bin/python ./test/unit/mysql_class/gtidset_ge.py
/usr/bin/python ./test/unit/mysql_class/gtidset_gt.py
/usr/bin/python ./test/unit/mysql_class/gtidset_le.py
/usr/bin/python ./test/unit/mysql_class/gtidset_lt.py
/usr/bin/python ./test/unit/mysql_class/gtidset_ne.py
/usr/bin/python ./test/unit/mysql_class/masterrep_connect.py
/usr/bin/python ./test/unit/mysql_class/masterrep_init.py
/usr/bin/python ./test/unit/mysql_class/masterrep_showslvhosts.py
/usr/bin/python ./test/unit/mysql_class/masterrep_getloginfo.py
/usr/bin/python ./test/unit/mysql_class/masterrep_updmststatus.py
/usr/bin/python ./test/unit/mysql_class/position_cmp.py
/usr/bin/python ./test/unit/mysql_class/rep_fetchdodb.py
/usr/bin/python ./test/unit/mysql_class/rep_fetchigndb.py
/usr/bin/python ./test/unit/mysql_class/rep_getservid.py
/usr/bin/python ./test/unit/mysql_class/rep_getservuuid.py
/usr/bin/python ./test/unit/mysql_class/rep_init.py
/usr/bin/python ./test/unit/mysql_class/rep_showslvhosts.py
/usr/bin/python ./test/unit/mysql_class/rep_showslvstate.py
/usr/bin/python ./test/unit/mysql_class/rep_startslave.py
/usr/bin/python ./test/unit/mysql_class/rep_stopslave.py
/usr/bin/python ./test/unit/mysql_class/rep_verify_srv_id.py
/usr/bin/python ./test/unit/mysql_class/server_chg_db.py
/usr/bin/python ./test/unit/mysql_class/server_connect.py
/usr/bin/python ./test/unit/mysql_class/server_disconnect.py
/usr/bin/python ./test/unit/mysql_class/server_fetchlogs.py
/usr/bin/python ./test/unit/mysql_class/server_fetchmstrepcfg.py
/usr/bin/python ./test/unit/mysql_class/server_fetchslvrepcfg.py
/usr/bin/python ./test/unit/mysql_class/server_flushlogs.py
/usr/bin/python ./test/unit/mysql_class/server_getname.py
/usr/bin/python ./test/unit/mysql_class/server_init.py
/usr/bin/python ./test/unit/mysql_class/server_is_connected.py
/usr/bin/python ./test/unit/mysql_class/server_reconnect.py
/usr/bin/python ./test/unit/mysql_class/server_set_pass_config.py
/usr/bin/python ./test/unit/mysql_class/server_set_ssl_config.py
/usr/bin/python ./test/unit/mysql_class/server_set_tls_config.py
/usr/bin/python ./test/unit/mysql_class/server_setsrvbinlogcrc.py
/usr/bin/python ./test/unit/mysql_class/server_setsrvgtid.py
/usr/bin/python ./test/unit/mysql_class/server_setup_ssl.py
/usr/bin/python ./test/unit/mysql_class/server_updlogstats.py
/usr/bin/python ./test/unit/mysql_class/server_updmstrepstat.py
/usr/bin/python ./test/unit/mysql_class/server_updsrvperf.py
/usr/bin/python ./test/unit/mysql_class/server_updslvrepstat.py
/usr/bin/python ./test/unit/mysql_class/server_updsrvstat.py
/usr/bin/python ./test/unit/mysql_class/server_vertsql.py
/usr/bin/python ./test/unit/mysql_class/slaverep_connect.py
/usr/bin/python ./test/unit/mysql_class/slaverep_init.py
/usr/bin/python ./test/unit/mysql_class/slaverep_fetchdotbl.py
/usr/bin/python ./test/unit/mysql_class/slaverep_fetchigntbl.py
/usr/bin/python ./test/unit/mysql_class/slaverep_updslvstatus.py
/usr/bin/python ./test/unit/mysql_class/slaverep_geterrstat.py
/usr/bin/python ./test/unit/mysql_class/slaverep_getloginfo.py
/usr/bin/python ./test/unit/mysql_class/slaverep_getothers.py
/usr/bin/python ./test/unit/mysql_class/slaverep_getthrstat.py
/usr/bin/python ./test/unit/mysql_class/slaverep_gettime.py
/usr/bin/python ./test/unit/mysql_class/slaverep_isslaveup.py
/usr/bin/python ./test/unit/mysql_class/slaverep_isslverror.py
/usr/bin/python ./test/unit/mysql_class/slaverep_isslvrunning.py
/usr/bin/python ./test/unit/mysql_class/slaverep_showslvstate.py
/usr/bin/python ./test/unit/mysql_class/slaverep_startslave.py
/usr/bin/python ./test/unit/mysql_class/slaverep_stopslave.py
/usr/bin/python ./test/unit/mysql_class/slaverep_updslvstate.py
/usr/bin/python ./test/unit/mysql_class/slaverep_updslvtime.py
/usr/bin/python ./test/unit/mysql_class/slaverep_updgtidpos.py

