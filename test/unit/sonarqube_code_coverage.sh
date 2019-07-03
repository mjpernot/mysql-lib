#!/bin/bash
# Unit test code coverage for SonarQube to cover all library modules.
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
coverage run -a --source=mysql_class test/unit/mysql_class/MasterRep_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/MasterRep_showslvhosts.py
coverage run -a --source=mysql_class test/unit/mysql_class/MasterRep_getloginfo.py
coverage run -a --source=mysql_class test/unit/mysql_class/MasterRep_updmststatus.py
coverage run -a --source=mysql_class test/unit/mysql_class/Position_cmp.py
coverage run -a --source=mysql_class test/unit/mysql_class/Rep_fetchdodb.py
coverage run -a --source=mysql_class test/unit/mysql_class/Rep_fetchigndb.py
coverage run -a --source=mysql_class test/unit/mysql_class/Rep_getservid.py
coverage run -a --source=mysql_class test/unit/mysql_class/Rep_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/Rep_showslvhosts.py
coverage run -a --source=mysql_class test/unit/mysql_class/Rep_showslvstate.py
coverage run -a --source=mysql_class test/unit/mysql_class/Rep_startslave.py
coverage run -a --source=mysql_class test/unit/mysql_class/Rep_stopslave.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_setsrvbinlogcrc.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_setsrvgtid.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_fetchmstrepcfg.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_fetchslvrepcfg.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_updmstrepstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_updslvrepstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_updsrvperf.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_updsrvstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_connect.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_disconnect.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_fetchlogs.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_flushlogs.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_vertsql.py
coverage run -a --source=mysql_class test/unit/mysql_class/Server_updlogstats.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_init.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_updslvstatus.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_geterrstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_getloginfo.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_getothers.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_getthrstat.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_gettime.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_isslaveup.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_isslverror.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_isslvrunning.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_showslvstate.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_startslave.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_stopslave.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_updslvstate.py
coverage run -a --source=mysql_class test/unit/mysql_class/SlaveRep_updslvtime.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/analyze_tbl.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/change_master_to.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/checksum.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/check_tbl.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/chg_slv_state.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/fetch_db_dict.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/fetch_logs.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/fetch_tbl_dict.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/optimize_tbl.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/purge_bin_logs.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/reset_master.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/reset_slave.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/select_wait_until.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/create_slv_array.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/crt_cmd.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/crt_srv_inst.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/fetch_slv.py
coverage run -a --source=mysql_libs test/unit/mysql_libs/find_name.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

