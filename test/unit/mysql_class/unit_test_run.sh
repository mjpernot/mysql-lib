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
test/unit/mysql_class/MasterRep_init.py
test/unit/mysql_class/MasterRep_showslvhosts.py
test/unit/mysql_class/MasterRep_getloginfo.py
test/unit/mysql_class/Position_cmp.py
test/unit/mysql_class/Rep_fetchdodb.py
test/unit/mysql_class/Rep_fetchigndb.py
test/unit/mysql_class/Rep_getservid.py
test/unit/mysql_class/Rep_init.py
test/unit/mysql_class/Rep_showslvhosts.py
test/unit/mysql_class/Rep_showslvstate.py
test/unit/mysql_class/Rep_startslave.py
test/unit/mysql_class/Rep_stopslave.py
test/unit/mysql_class/Server_init.py
test/unit/mysql_class/Server_setsrvbinlogcrc.py
test/unit/mysql_class/Server_setsrvgtid.py
test/unit/mysql_class/Server_fetchmstrepcfg.py
test/unit/mysql_class/Server_fetchslvrepcfg.py
test/unit/mysql_class/Server_updmstrepstat.py
test/unit/mysql_class/Server_updslvrepstat.py
test/unit/mysql_class/Server_updsrvperf.py
test/unit/mysql_class/Server_updsrvstat.py
test/unit/mysql_class/Server_connect.py
test/unit/mysql_class/Server_disconnect.py
test/unit/mysql_class/Server_fetchlogs.py
test/unit/mysql_class/Server_flushlogs.py
test/unit/mysql_class/Server_vertsql.py
test/unit/mysql_class/Server_updlogstats.py

