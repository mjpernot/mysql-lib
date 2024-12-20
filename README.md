# Python project that contains common libraries and classes for MySQL database.
# Classification (U)

# Description:
  This project consists of a number of Python files that contain common function libraries and classes for connecting to and operating in a MySQL database and Mysql replication set.


###  This README file is broken down into the following sections:
  * Prerequisites
  * Installation
    - Pip Installation
  * Testing
    - Git Installation
    - Unit
    - Integration


# Prerequisites:

  * List of Linux packages that need to be installed on the server via git.
    - python3-pip


# Installation:

### Pip Installation:

###### Create requirements file in another program's project to install mysql-lib as a library module.

  * Create requirements-mysql-lib.txt and requirements-mysql-python-lib.txt.  Replace N.N.N with the version of the library needed.

```
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/mysql-lib.git@N.N.N#egg=mysql-lib' > requirements-mysql-lib.txt
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git@N.N.N#egg=python-lib' > requirements-mysql-python-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file and the following lines to install the library modules:

```
python -m pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general mysql-Lib requirements (requirements3.txt) to the other program's requirements3.txt file.


# Testing

### Git Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-lib.git
```

Install/upgrade system modules.

NOTE: Install as the user that will use the package.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Install supporting classes and libraries

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit Testing:

### Installation:

Install the project using the procedures in the Git Installation section.

### Testing:

```
test/unit/mysql_libs/unit_test_run.sh
test/unit/mysql_class/unit_test_run.sh
```

### Code Coverage:
```
test/unit/mysql_libs/code_coverage.sh
test/unit/mysql_class/code_coverage.sh
```

# Integration Testing:

NOTE:  Integration testing will require access to a MySQL database server.

### Installation:

Install the project using the procedures in the Git Installation section.

### Configuration:

Create MySQL configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "DIRECTORY_PATH/my.cnf"
    - ssl_disabled = True

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

```
cp mysql_cfg.py test/integration/config
vim test/integration/config/mysql_cfg.py
chmod 600 test/integration/config/mysql_cfg.py
```

Create MySQL definition file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
cp mysql.cfg test/integration/config
vim test/integration/config/mysql.cfg
chmod 600 test/integration/config/mysql.cfg
```

### Testing:

```
test/integration/mysql_libs/integration_test_run.sh
test/integration/mysql_class/integration_test_run.sh
```

### Code Coverage:
```
test/integration/mysql_libs/code_coverage.sh
test/integration/mysql_class/code_coverage.sh
```

### Master Replication Testing Section

This section requires the database being tested to be a master database in a MySQL replica set.  Will include all previous testing units.

### Configuration:

Create MySQL configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PSWORD"
    - rep_user = "REP_USER"
    - rep_japd = "REP_PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "DIRECTORY_PATH/my.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

```
cp mysql_cfg.py test/integration/config/master_mysql_cfg.py
vim test/integration/config/master_mysql_cfg.py
chmod 600 test/integration/config/master_mysql_cfg.py
```

Create MySQL definition file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
cp mysql.cfg test/integration/config
vim test/integration/config/mysql.cfg
chmod 600 test/integration/config/mysql.cfg
```

### Testing:

```
test/integration/mysql_class/rep_integration_test_run.sh
```

### Code Coverage:
```
test/integration/mysql_class/rep_code_coverage.sh
```

### Slave Replication Testing Section

This section requires the database being tested to be a slave database in a MySQL replica set.

Testing will also require a master_mysql_cfg.py file to be present in the config directory.  See above for details on creating one.

### Configuration:

Create MySQL configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PSWORD"
    - rep_user = "REP_USER"
    - rep_japd = "REP_PSWORD"
    - host = "HOST_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "DIRECTORY_PATH/my.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

```
cp mysql_cfg.py test/integration/config/slave_mysql_cfg.py
vim test/integration/config/slave_mysql_cfg.py
chmod 600 test/integration/config/slave_mysql_cfg.py
```

Create MySQL definition file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
cp mysql.cfg test/integration/config
vim test/integration/config/mysql.cfg
chmod 600 test/integration/config/mysql.cfg
```

Create a MySQL slave configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL slave setup:
    - user = USER
    - japd = PSWORD
    - rep_user = REP_USER
    - rep_japd = REP_PSWORD
    - host = HOST_IP
    - name = HOSTNAME
    - sid = SERVER_ID

  * Change these entries only if required:
    - cfg_file = None
    - serv_os = Linux
    - port = 3306

  * NOTE:  Create a new set of entries for each slave in the MySQL replica set.

```
cp slave.txt test/integration/config
vim test/integration/config/slave.txt
chmod 600 test/integration/config/slave.txt
```

### Testing:

```
test/integration/mysql_class/slaverep_integration_test_run.sh
```

### Code Coverage:
```
test/integration/mysql_class/slaverep_code_coverage.sh
```

