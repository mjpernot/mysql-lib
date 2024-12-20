# Classification (U)

"""Program:  server_fetchslvrepcfg.py

    Description:  Unit testing of Server.fetch_slv_rep_cfg in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_fetchslvrepcfg.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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

    def test_post_8026(self):

        """Function:  test_post_8026

        Description:  Test with post-MySQL 8.0.26.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.version = (8, 0, 28)

        self.assertEqual(
            mysqldb.fetch_slv_rep_cfg(), (
                {"log_bin": None, "sync_relay_log": None, "read_only": None,
                 "sync_source_info": None, "log_replica_updates": None,
                 "sync_relay_log_info": None}))

    def test_pre_8026(self):

        """Function:  test_pre_8026

        Description:  Test with pre-MySQL 8.0.26.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.version = (8, 0, 21)

        self.assertEqual(
            mysqldb.fetch_slv_rep_cfg(), (
                {"log_bin": None, "sync_relay_log": None, "read_only": None,
                 "sync_master_info": None, "log_slave_updates": None,
                 "sync_relay_log_info": None}))

    def test_value(self):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqldb.version = (8, 0, 21)

        self.assertEqual(
            mysqldb.fetch_slv_rep_cfg(), (
                {"log_bin": None, "sync_relay_log": None, "read_only": None,
                 "sync_master_info": None, "log_slave_updates": None,
                 "sync_relay_log_info": None}))


if __name__ == "__main__":
    unittest.main()
