#!/usr/bin/python
# Classification (U)

"""Program:  MasterRep_init.py

    Description:  Unit testing of MasterRep.__init__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/MasterRep_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mysql_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_rep_user -> Test with rep user settings.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_pwd"
        self.machine = "Linux"
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"
        self.rep_user = "rep_user"
        self.rep_pswd = "rep_pswd"

    def test_rep_user(self):

        """Function:  test_rep_user

        Description:  Test with rep user settings.

        Arguments:

        """

        mysqlrep = mysql_class.MasterRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            machine=self.machine, defaults_file=self.defaults_file,
            rep_user=self.rep_user, rep_pswd = self.rep_pswd)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port, mysqlrep.rep_user, mysqlrep.rep_pswd),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306, self.rep_user, self.rep_pswd))

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mysqlrep = mysql_class.MasterRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            machine=self.machine, defaults_file=self.defaults_file)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306))


if __name__ == "__main__":
    unittest.main()
