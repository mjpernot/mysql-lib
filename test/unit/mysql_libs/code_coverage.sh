#!/bin/bash
# Unit test code coverage for module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
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

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
