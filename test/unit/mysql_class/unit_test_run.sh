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
test/unit/mysql_class/gtidset_or.py
test/unit/mysql_class/gtidset_init.py
test/unit/mysql_class/gtidset_str.py
test/unit/mysql_class/gtidset_union.py
test/unit/mysql_class/gtidset_eq.py
test/unit/mysql_class/gtidset_ge.py
test/unit/mysql_class/gtidset_gt.py
test/unit/mysql_class/gtidset_le.py
test/unit/mysql_class/gtidset_lt.py
test/unit/mysql_class/gtidset_ne.py
test/unit/mysql_class/masterrep_connect.py
test/unit/mysql_class/MasterRep_init.py
test/unit/mysql_class/MasterRep_showslvhosts.py
test/unit/mysql_class/MasterRep_getloginfo.py
test/unit/mysql_class/MasterRep_updmststatus.py
test/unit/mysql_class/Position_cmp.py
test/unit/mysql_class/Rep_fetchdodb.py
test/unit/mysql_class/Rep_fetchigndb.py
test/unit/mysql_class/Rep_getservid.py
test/unit/mysql_class/Rep_init.py
test/unit/mysql_class/Rep_showslvhosts.py
test/unit/mysql_class/Rep_showslvstate.py
test/unit/mysql_class/Rep_startslave.py
test/unit/mysql_class/Rep_stopslave.py
test/unit/mysql_class/server_chg_db.py
test/unit/mysql_class/server_connect.py
test/unit/mysql_class/server_disconnect.py
test/unit/mysql_class/server_fetchlogs.py
test/unit/mysql_class/server_fetchmstrepcfg.py
test/unit/mysql_class/server_fetchslvrepcfg.py
test/unit/mysql_class/server_flushlogs.py
test/unit/mysql_class/server_getname.py
test/unit/mysql_class/server_init.py
test/unit/mysql_class/server_is_connected.py
test/unit/mysql_class/server_reconnect.py
test/unit/mysql_class/server_setsrvbinlogcrc.py
test/unit/mysql_class/server_setsrvgtid.py
test/unit/mysql_class/server_updlogstats.py
test/unit/mysql_class/server_updmstrepstat.py
test/unit/mysql_class/server_updsrvperf.py
test/unit/mysql_class/server_updslvrepstat.py
test/unit/mysql_class/server_updsrvstat.py
test/unit/mysql_class/server_vertsql.py
test/unit/mysql_class/slaverep_connect.py
test/unit/mysql_class/SlaveRep_init.py
test/unit/mysql_class/SlaveRep_fetchdotbl.py
test/unit/mysql_class/SlaveRep_fetchigntbl.py
test/unit/mysql_class/SlaveRep_updslvstatus.py
test/unit/mysql_class/SlaveRep_geterrstat.py
test/unit/mysql_class/SlaveRep_getloginfo.py
test/unit/mysql_class/SlaveRep_getothers.py
test/unit/mysql_class/SlaveRep_getthrstat.py
test/unit/mysql_class/SlaveRep_gettime.py
test/unit/mysql_class/SlaveRep_isslaveup.py
test/unit/mysql_class/SlaveRep_isslverror.py
test/unit/mysql_class/SlaveRep_isslvrunning.py
test/unit/mysql_class/SlaveRep_showslvstate.py
test/unit/mysql_class/SlaveRep_startslave.py
test/unit/mysql_class/SlaveRep_stopslave.py
test/unit/mysql_class/SlaveRep_updslvstate.py
test/unit/mysql_class/SlaveRep_updslvtime.py
test/unit/mysql_class/SlaveRep_updgtidpos.py

