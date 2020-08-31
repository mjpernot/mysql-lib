# Python project that contains common libraries and classes for MySQL database.
# Classification (U)

# Description:
  This project consists of a number of Python files that contain common function libraries and classes for connecting to and operating in a MySQL database and Mysql replication set.


###  This README file is broken down into the following sections:
  * Prerequisites
  * Installation
    - Pip Installation
    - Git Installation
  * Testing
    - Unit
    - Integration


# Prerequisites:

  * List of Linux packages that need to be installed on the server via git.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/machine
    - lib/gen_libs


# Installation:
  There are two types of installs: pip and git.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

###### Create requirements file in another program's project to install mysql-lib as a library module.

Create requirements-mysql-lib.txt file:
```
vim {Other_Python_Project}/requirements-mysql-lib.txt
```

Add the following lines to the requirements-mysql-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/mysql-lib.git#egg=mysql-lib
```

Create requirements-python-lib.txt file:
```
vim {Other_Python_Project}/requirements-python-lib.txt
```

Add the following lines to the requirements-python-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/python-lib.git#egg=python-lib
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file:
```
vim {Other_Python_Project}/README.md
```

Add the following lines under the "Install supporting classes and libraries" section.
```
   pip install -r requirements-mysql-lib.txt --target mysql_lib --trusted-host pypi.appdev.proj.coe.ic.gov
   pip install -r requirements-python-lib.txt --target mysql_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general Mysql-Lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Modify the requirements.txt file:
```
vim {Other_Python_Project}/requirements.txt
```

Add the following lines to the requirements.txt file:
```
mysql-connector-python==8.0.16
simplejson==2.0.9
```


### Git Installation:

Install general Python libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mysql-lib.git
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries

```
cd mysql-lib
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Testing

# Unit Testing:

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
cd mysql-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

### Testing mysql_class.py:

```
cd {Python_Project}/mysql-lib
test/unit/mysql_class/unit_test_run.sh
```

### Code Coverage mysql_class.py:
```
cd {Python_Project}/mysql-lib
test/unit/mysql_class/code_coverage.sh
```

### Testing mysql-lib.py:

```
cd {Python_Project}/mysql-lib
test/unit/mysql_libs/unit_test_run.sh
```

### Code Coverage mysql-lib.py:
```
cd {Python_Project}/mysql-lib
test/unit/mysql_libs/code_coverage.sh
```

# Integration Testing:

NOTE:  Integration testing will require access to a MySQL database server.

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
cd mysql-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

### Configuration:

Create MySQL configuration file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL setup:
    - user = "USER"
    - japd = "PASSWORD"
    - host = "SERVER_IP"
    - name = "HOST_NAME"
    - sid = SERVER_ID
    - extra_def_file = "PYTHON_PROJECT/config/mysql.cfg"
    - cfg_file = "DIRECTORY_PATH/my.cnf"

  * Change these entries only if required:
    - serv_os = "Linux"
    - port = 3306

```
cd test/integration/config
cp mysql_cfg.py.TEMPLATE mysql_cfg.py
vim mysql_cfg.py
chmod 600 mysql_cfg.py
```

Create MySQL definition file.

Make the appropriate change to the environment.
  * Change these entries in the MySQL definition file:
    - password="PASSWORD"
    - socket=DIRECTORY_PATH/mysql.sock

```
cp mysql.cfg.TEMPLATE mysql.cfg
vim mysql.cfg
chmod 600 mysql.cfg
```

### Testing mysql_class.py:

```
cd {Python_Project}/mysql-lib
test/integration/mysql_class/integration_test_run.sh
```

### Code Coverage mysql_class.py:
```
cd {Python_Project}/mysql-lib
test/integration/mysql_class/code_coverage.sh
```

### Testing mysql-lib.py:

```
cd {Python_Project}/mysql-lib
test/integration/mysql_libs/integration_test_run.sh
```

### Code Coverage mysql-lib.py:
```
cd {Python_Project}/mysql-lib
test/integration/mysql_libs/code_coverage.sh
```

### Replication Testing Section

This section requires the database being tested to be a master database in a MySQL replica set.  Will include all previous testing units.

### Testing mysql_class.py:

```
cd {Python_Project}/mysql-lib
test/integration/mysql_class/rep_integration_test_run.sh
```

### Code Coverage mysql_class.py:
```
cd {Python_Project}/mysql-lib
test/integration/mysql_class/rep_code_coverage.sh
```

