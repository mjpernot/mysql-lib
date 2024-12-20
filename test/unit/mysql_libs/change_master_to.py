# Classification (U)

"""Program:  change_master_to.py

    Description:  Unit testing of change_master_to in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/change_master_to.py

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
import mysql_libs                           # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():                             # pylint:disable=R0903

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__
        cmd_sql

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = True
        self.host = "hostname"
        self.port = 3306
        self.sql_user = "sqluser"
        self.sql_pass = "japd"
        self.file = "binlog-filename"
        self.pos = "file-position"
        self.name = "server-name"
        self.rep_user = "rep_user"
        self.rep_japd = "rep_japd"
        self.cmd = None
        self.version = (8, 0, 28)

    def cmd_sql(self, cmd):

        """Method:  cmd_sql

        Description:  Stub holder for Server.cmd_sql method.

        Arguments:
            (input) cmd

        """

        self.cmd = cmd

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_version_difference2
        test_version_difference
        test_post_8023
        test_pre_8023
        test_ssl_on2
        test_ssl_on
        test_ssl_off2
        test_ssl_off
        test_ssl_empty_return2
        test_ssl_empty_return
        test_change_master_to_non_gtid
        test_change_master_to_gtid

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.master = Server()
        self.slave = Server()
        self.fetch = {}
        self.fetch2 = {"require_secure_transport": "OFF"}
        self.fetch3 = {"require_secure_transport": "ON"}

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_version_difference2(self, mock_fetch):

        """Function:  test_version_difference2

        Description:  Test with two different MySQL versions.

        Arguments:

        """

        self.master.version = (8, 0, 21)
        self.slave.version = (8, 0, 28)

        mock_fetch.return_value = self.fetch

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_version_difference(self, mock_fetch):

        """Function:  test_version_difference

        Description:  Test with two different MySQL versions.

        Arguments:

        """

        self.master.version = (8, 0, 28)
        self.slave.version = (8, 0, 21)

        mock_fetch.return_value = self.fetch

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_post_8023(self, mock_fetch):

        """Function:  test_post_8023

        Description:  Test with post-MySQL 8.0.23 version.

        Arguments:

        """

        self.master.version = (8, 0, 28)
        self.slave.version = (8, 0, 28)

        mock_fetch.return_value = self.fetch

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_pre_8023(self, mock_fetch):

        """Function:  test_pre_8023

        Description:  Test with pre-MySQL 8.0.23 version.

        Arguments:

        """

        self.master.version = (8, 0, 21)
        self.slave.version = (8, 0, 21)

        mock_fetch.return_value = self.fetch

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_ssl_on2(self, mock_fetch):

        """Function:  test_ssl_on2

        Description:  Test with SSL returned with secure transport set to on.

        Arguments:

        """

        mock_fetch.return_value = self.fetch3

        self.master.gtid_mode = None

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_ssl_on(self, mock_fetch):

        """Function:  test_ssl_on

        Description:  Test with SSL returned with secure transport set to on.

        Arguments:

        """

        mock_fetch.return_value = self.fetch3

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_ssl_off2(self, mock_fetch):

        """Function:  test_ssl_off2

        Description:  Test with SSL returned with secure transport set to off.

        Arguments:

        """

        mock_fetch.return_value = self.fetch2

        self.master.gtid_mode = None

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_ssl_off(self, mock_fetch):

        """Function:  test_ssl_off

        Description:  Test with SSL returned with secure transport set to off.

        Arguments:

        """

        mock_fetch.return_value = self.fetch2

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_ssl_empty_return2(self, mock_fetch):

        """Function:  test_ssl_empty_return2

        Description:  Test with SSL returned with no data.

        Arguments:

        """

        mock_fetch.return_value = self.fetch

        self.master.gtid_mode = None

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_ssl_empty_return(self, mock_fetch):

        """Function:  test_ssl_empty_return

        Description:  Test with SSL returned with no data.

        Arguments:

        """

        mock_fetch.return_value = self.fetch

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_change_master_to_non_gtid(self, mock_fetch):

        """Function:  test_change_master_to_non_gtid

        Description:  Test in gtid_mode off.

        Arguments:

        """

        mock_fetch.return_value = self.fetch

        self.master.gtid_mode = None

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))

    @mock.patch("mysql_libs.mysql_class.fetch_sys_var")
    def test_change_master_to_gtid(self, mock_fetch):

        """Function:  test_change_master_to_gtid

        Description:  Test in gtid_mode on.

        Arguments:

        """

        mock_fetch.return_value = self.fetch

        with gen_libs.no_std_out():
            self.assertFalse(
                mysql_libs.change_master_to(self.master, self.slave))


if __name__ == "__main__":
    unittest.main()
