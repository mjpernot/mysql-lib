# Python project that contains common libraries and classes for MySQL database.
# Classification (U)

# Description:
  This project consists of a number of Python files that contain common function libraries and classes for connecting to and operating in a MySQL database and Mysql replication set.


###  This README file is broken down into the following sections:
  * Prerequisites
  * Installation
  * Testing
    - Unit


# Prerequisites:

  * List of Linux packages that need to be installed on the server via git.
    - python-libs
    - python-devel
    - git
    - python-pip
    - mysql-connector-python
    - mysql-utilities

  * Local class/library dependencies within the program structure.
    - lib/machine
    - lib/errors
    - lib/gen_libs


# Installation:
  There are two types of installs: pip and git.  Pip will only install the program modules and classes, whereas git will install all modules and classes including testing programs along with README and CHANGELOG files.  The Pip installation will be modifying another program's project to install these supporting librarues via pip.

### Pip Installation:
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

Create requirement files for the supporting library in another program's project.

```
cd {Python_Project}
cat requirements-mysql-lib.txt >> {Other_Python_Project}/requirements-mysql-lib.txt
cat requirements-python-lib.txt >> {Other_Python_Project}/requirements-python-lib.txt
```

Place the following command into the another program's README.md file under the "Install supporting classes and libraries" section.
   pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov

```
vim {Other_Python_Project}/README.md
```

Add the system module requirements to the another program's requirements.txt file and remove any duplicates.

``
cat requirements.txt >> {Other_Python_Project}/requirements.txt
vim {Other_Python_Project}/requirements.txt
```

### Git Installation:

Install general Python libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-lib.git
```

Install supporting classes and libraries

```
cd mysql-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```


# Testing

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the library modules and methods in the classes.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-lib.git
```

Install/upgrade system modules.

```
cd python-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

# Unit test runs for mysql_class.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mysql-lib
```

### Unit:  
```
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
test/unit/mysql_class/SlaveRep_init.py
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
test/unit/mysql_libs/analyze_tbl.py
test/unit/mysql_libs/change_master_to.py
```

### All unit testing for mysql_class.py:
```
test/unit/mysql_class/unit_test_run.sh
```

### Unit test code coverage
```
test/unit/mysql_class/code_coverage.sh
```

# Unit test runs for mysql-lib.py:

### Unit:  
```
test/unit/mysql_lib/
```

### All unit testing for mysql_lib.py:
```
test/unit/mysql_lib/unit_test_run.sh
```

### Unit test code coverage
```
test/unit/mysql_lib/code_coverage.sh
```

