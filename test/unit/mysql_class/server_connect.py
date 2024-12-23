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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import lib.gen_libs as gen_libs             # pylint:disable=E0401,R0402,C0413
import lib.machine as machine               # pylint:disable=E0401,R0402,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                             # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__
        disconnect

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialize environment.

        Arguments:

        """

        self.version = (5, 7, 33)

    def get_server_version(self):

        """Function:  get_server_version

        Description:  Test of get_server_version function.

        Arguments:

        """

        return self.version


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_version
        test_silent_exception2
        test_silent_exception
        test_database
        test_config
        test_connect_exception
        test_connect

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
        self.results = "Couldn't connect to database."
        self.mysql = Server()

    @mock.patch("mysql_class.mysql.connector.connect")
    def test_version(self, mock_connect):

        """Function:  test_version

        Description:  Test with version attribute.

        Arguments:

        """

        mock_connect.return_value = self.mysql

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.connect()

        self.assertEqual(mysqldb.version, (5, 7, 33))

    def test_silent_exception2(self):

        """Function:  test_silent_exception2

        Description:  Test silent connection method exception.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.connect(silent=True)

        self.assertEqual(mysqldb.conn_msg[:29], self.results)

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

        mock_connect.return_value = self.mysql
        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.connect(database=self.database))

    @mock.patch("mysql_class.mysql.connector.connect")
    def test_config2(self, mock_connect):

        """Function:  test_config2

        Description:  Test with config attribute.

        Arguments:

        """

        mock_connect.return_value = self.mysql
        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertEqual(mysqldb.config, self.config)

    @mock.patch("mysql_class.mysql.connector.connect")
    def test_config(self, mock_connect):

        """Function:  test_config

        Description:  Test with config attribute.

        Arguments:

        """

        mock_connect.return_value = self.mysql

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.connect())

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

        mock_connect.return_value = self.mysql
        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.connect())


if __name__ == "__main__":
    unittest.main()
