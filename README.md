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
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/machine
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
test/unit/mysql_lib/unit_test_run.sh
```

### Code Coverage mysql-lib.py:
```
cd {Python_Project}/mysql-lib
test/unit/mysql_lib/code_coverage.sh
```

