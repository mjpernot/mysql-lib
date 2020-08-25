#!/usr/bin/python
# Classification (U)

"""Program:  Server_init.py

    Description:  Unit testing of Server.__init__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/Server_init.py

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
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_no_host -> Test with no host arg.
        test_host -> Test with passing host arg.
        test_no_default -> Test with no default file.
        test_default -> Test with default file.

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
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"
        self.results = self.machine.defaults_file

    def test_no_host(self):

        """Function:  test_no_host

        Description:  Test with no host arg.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.defaults_file, self.results)

    def test_host(self):

        """Function:  test_host

        Description:  Test with passing host arg.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, host=self.host)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user,
             mysqldb.sql_pass, mysqldb.machine, mysqldb.host, mysqldb.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, self.host, 3306))

    def test_no_default(self):

        """Function:  test_no_default

        Description:  Test with no default file.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.defaults_file, self.results)

    def test_default(self):

        """Function:  test_default

        Description:  Test with default file.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user,
             mysqldb.sql_pass, mysqldb.machine, mysqldb.host, mysqldb.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306))


if __name__ == "__main__":
    unittest.main()
