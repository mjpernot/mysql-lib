# Classification (U)

"""Program:  slaverep_startslave.py

    Description:  Unit testing of SlaveRep.start_slave in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_startslave.py

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
        test_none_secsbehind
        test_int_secsbehind
        test_string_secsbehind
        test_except_secsbehind -> Test raising exception: Seconds_Behind_Master
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
            {"Slave_IO_State": "Up", "Seconds_Behind_Master": "20"}]
        self.show_stat2 = [
            {"Replica_IO_State": "Up", "Seconds_Behind_Source": "20"}]

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_post_8022(self, mock_stat):

        """Function:  test_post_8022

        Description:  Test with post-MySQL 8.0.22.

        Arguments:

        """

        self.show_stat2[0]["Seconds_Behind_Source"] = None

        mock_stat.return_value = self.show_stat2

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 28)
        mysqlrep.start_slave()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.secs_behind), ("Up", "null"))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_pre_8022(self, mock_stat):

        """Function:  test_pre_8022

        Description:  Test with pre-MySQL 8.0.22.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = None

        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 21)
        mysqlrep.start_slave()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.secs_behind), ("Up", "null"))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_none_secsbehind(self, mock_stat):

        """Function:  test_none_secsbehind

        Description:  Test None for Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = None

        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 21)
        mysqlrep.start_slave()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.secs_behind), ("Up", "null"))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_int_secsbehind(self, mock_stat):

        """Function:  test_int_secsbehind

        Description:  Test integer for Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = 20

        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 21)
        mysqlrep.start_slave()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.secs_behind), ("Up", 20))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_string_secsbehind(self, mock_stat):

        """Function:  test_string_secsbehind

        Description:  Test string for Seconds_Behind_Master.

        Arguments:

        """

        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 21)
        mysqlrep.start_slave()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.secs_behind), ("Up", 20))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_except_secsbehind(self, mock_stat):

        """Function:  test_except_secsbehind

        Description:  Test raising exception: Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = "time"

        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = (8, 0, 21)
        mysqlrep.start_slave()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.secs_behind), ("Up", "null"))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
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
        mysqlrep.start_slave()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.secs_behind), ("Up", 20))


if __name__ == "__main__":
    unittest.main()
