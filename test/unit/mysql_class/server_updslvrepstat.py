# Classification (U)

"""Program:  server_updslvrepstat.py

    Description:  Unit testing of Server.upd_slv_rep_stat in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_updslvrepstat.py

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
import lib.machine as machine               # pylint:disable=E0401,R0402,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_post_8026
        test_pre_8026
        test_value

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

    @mock.patch("mysql_class.fetch_sys_var")
    def test_post_8026(self, mock_sysvar):

        """Function:  test_post_8026

        Description:  Test with post-MySQL 8.0.26.

        Arguments:

        """

        mock_sysvar.side_effect = [
            {"log_bin": "ON"}, {"read_only": "YES"},
            {"log_replica_updates": "YES"}, {"sync_source_info": "NO"},
            {"sync_relay_log": "ON"}, {"sync_relay_log_info": "YES"}]

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.version = (8, 0, 28)

        mysqldb.upd_slv_rep_stat()

        self.assertEqual(
            (mysqldb.log_bin, mysqldb.sync_rly_info), ("ON", "YES"))

    @mock.patch("mysql_class.fetch_sys_var")
    def test_pre_8026(self, mock_sysvar):

        """Function:  test_pre_8026

        Description:  Test with pre-MySQL 8.0.26.

        Arguments:

        """

        mock_sysvar.side_effect = [
            {"log_bin": "ON"}, {"read_only": "YES"},
            {"log_slave_updates": "YES"}, {"sync_master_info": "NO"},
            {"sync_relay_log": "ON"}, {"sync_relay_log_info": "YES"}]

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.version = (8, 0, 21)

        mysqldb.upd_slv_rep_stat()

        self.assertEqual(
            (mysqldb.log_bin, mysqldb.sync_rly_info), ("ON", "YES"))

    @mock.patch("mysql_class.fetch_sys_var")
    def test_value(self, mock_sysvar):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_sysvar.side_effect = [
            {"log_bin": "ON"}, {"read_only": "YES"},
            {"log_slave_updates": "YES"}, {"sync_master_info": "NO"},
            {"sync_relay_log": "ON"}, {"sync_relay_log_info": "YES"}]

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.version = (8, 0, 21)

        mysqldb.upd_slv_rep_stat()

        self.assertEqual(
            (mysqldb.log_bin, mysqldb.sync_rly_info), ("ON", "YES"))


if __name__ == "__main__":
    unittest.main()
