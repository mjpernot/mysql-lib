# Classification (U)

"""Program:  slaverep_isslvrunning.py

    Description:  Unit testing of SlaveRep.is_slv_running in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_isslvrunning.py

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
        test_slv_both_true
        test_slv_two_true
        test_slv_run_true
        test_slv_sql_true
        test_slv_io_true
        test_default

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

    @mock.patch("mysql_class.SlaveRep.upd_slv_status")
    def test_slv_all_true(self, mock_upd):

        """Function:  test_slv_all_true

        Description:  Test with all attrs set to True.

        Arguments:

        """

        mock_upd.return_value = True

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "Yes"
        mysqlrep.slv_io = "Yes"
        mysqlrep.run = "Yes"

        self.assertTrue(mysqlrep.is_slv_running())

    @mock.patch("mysql_class.SlaveRep.upd_slv_status")
    def test_slv_two_true(self, mock_upd):

        """Function:  test_slv_two_true

        Description:  Test with two attrs set to True.

        Arguments:

        """

        mock_upd.return_value = True

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "Yes"
        mysqlrep.slv_io = "Yes"
        mysqlrep.run = "No"

        self.assertFalse(mysqlrep.is_slv_running())

    @mock.patch("mysql_class.SlaveRep.upd_slv_status")
    def test_slv_run_true(self, mock_upd):

        """Function:  test_slv_run_true

        Description:  Test with run set to True.

        Arguments:

        """

        mock_upd.return_value = True

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "No"
        mysqlrep.slv_io = "No"
        mysqlrep.run = "Yes"

        self.assertFalse(mysqlrep.is_slv_running())

    @mock.patch("mysql_class.SlaveRep.upd_slv_status")
    def test_slv_sql_true(self, mock_upd):

        """Function:  test_slv_sql_true

        Description:  Test with slv_sql set to True.

        Arguments:

        """

        mock_upd.return_value = True

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "Yes"
        mysqlrep.slv_io = "No"
        mysqlrep.run = "No"

        self.assertFalse(mysqlrep.is_slv_running())

    @mock.patch("mysql_class.SlaveRep.upd_slv_status")
    def test_slv_io_true(self, mock_upd):

        """Function:  test_slv_io_true

        Description:  Test with slv_io set to True.

        Arguments:

        """

        mock_upd.return_value = True

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "No"
        mysqlrep.run = "No"
        mysqlrep.slv_io = "Yes"

        self.assertFalse(mysqlrep.is_slv_running())

    @mock.patch("mysql_class.SlaveRep.upd_slv_status")
    def test_default(self, mock_upd):

        """Function:  test_default

        Description:  Test show_slv_state method.

        Arguments:

        """

        mock_upd.return_value = True

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "No"
        mysqlrep.run = "No"
        mysqlrep.slv_io = "No"

        self.assertFalse(mysqlrep.is_slv_running())


if __name__ == "__main__":
    unittest.main()
