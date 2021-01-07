#!/usr/bin/python
# Classification (U)

"""Program:  server_connect.py

    Description:  Unit testing of Server.connect in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_connect.py

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
import mock

# Local
sys.path.append(os.getcwd())
import mysql_class
import lib.gen_libs as gen_libs
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_silent_exception2 -> Test silent connection method exception.
        test_silent_exception -> Test silent connection method exception.
        test_database -> Test with database argument passed.
        test_config -> Test with config attribute.
        test_connect_exception -> Test connection method exception.
        test_connect -> Test connect method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        key1 = "pass"
        key2 = "wd"
        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"
        self.config = {key1 + key2: self.sql_pass}
        self.database = "minedatabase"
        errnum = 1045
        errmsg = "1045 (28000): Access denied for user \
'mysql_user'@'localhost' (using password: YES)"
        self.results = "Couldn't connect to database.  MySQL error %d: %s" \
                       % (errnum, errmsg)

    def test_silent_exception2(self):

        """Function:  test_silent_exception2

        Description:  Test silent connection method exception.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.connect(silent=True)

        self.assertEqual(mysqldb.conn_msg, self.results)

    def test_silent_exception(self):

        """Function:  test_silent_exception

        Description:  Test silent connection method exception.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.connect(silent=True))

    @mock.patch("mysql_class.mysql.connector.connect")
    def test_database(self, mock_connect):

        """Function:  test_database

        Description:  Test with database argument passed.

        Arguments:

        """

        mock_connect.return_value = True
        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.connect(database=self.database))

    @mock.patch("mysql_class.mysql.connector.connect")
    def test_config(self, mock_connect):

        """Function:  test_config

        Description:  Test with config attribute.

        Arguments:

        """

        mock_connect.return_value = True
        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.connect())
        self.assertEqual(mysqldb.config, self.config)

    def test_connect_exception(self):

        """Function:  test_connect_exception

        Description:  Test connection method exception.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        with gen_libs.no_std_out():
            self.assertFalse(mysqldb.connect())

    @mock.patch("mysql_class.mysql.connector.connect")
    def test_connect(self, mock_connect):

        """Function:  test_connect

        Description:  Test connect method.

        Arguments:

        """

        mock_connect.return_value = True
        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.connect())


if __name__ == "__main__":
    unittest.main()
