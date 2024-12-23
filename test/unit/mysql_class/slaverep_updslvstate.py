# Classification (U)

"""Program:  slaverep_updslvstate.py

    Description:  Unit testing of SlaveRep.upd_slv_state in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_updslvstate.py

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
        test_post_8022
        test_pre_8022
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

        self.show_stat = [
            {"Slave_IO_State": "Up", "Slave_IO_Running": "Running",
             "Slave_SQL_Running": "SQL_Code"}]
        self.show_stat2 = [
            {"Replica_IO_State": "Up", "Replica_IO_Running": "Running",
             "Replica_SQL_Running": "SQL_Code"}]

    @mock.patch("mysql_class.show_slave_stat")
    def test_post_8022(self, mock_stat):

        """Function:  test_post_8022

        Description:  Test with post-MySQL 8.0.22.

        Arguments:

        """

        mock_stat.return_value = self.show_stat2

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 28)
        mysqlrep.upd_slv_state()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.slv_io, mysqlrep.slv_sql),
            ("Up", "Running", "SQL_Code"))

    @mock.patch("mysql_class.show_slave_stat")
    def test_pre_8022(self, mock_stat):

        """Function:  test_pre_8022

        Description:  Test with pre-MySQL 8.0.22.

        Arguments:

        """

        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 21)
        mysqlrep.upd_slv_state()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.slv_io, mysqlrep.slv_sql),
            ("Up", "Running", "SQL_Code"))

    @mock.patch("mysql_class.show_slave_stat")
    def test_value(self, mock_stat):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 21)
        mysqlrep.upd_slv_state()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.slv_io, mysqlrep.slv_sql),
            ("Up", "Running", "SQL_Code"))


if __name__ == "__main__":
    unittest.main()
