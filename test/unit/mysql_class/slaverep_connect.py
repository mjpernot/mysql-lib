# Classification (U)

"""Program:  slaverep_connect.py

    Description:  Unit testing of SlaveRep.connect method in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_connect.py

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
        test_silent_true
        test_silent_false
        test_silent_default
        test_db_up
        test_db_down

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

        self.mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

    @mock.patch("mysql_class.Server.connect")
    def test_silent_true(self, mock_server):

        """Function:  test_silent_true

        Description:  Test with silent true set.

        Arguments:

        """

        mock_server.return_value = True

        self.assertFalse(self.mysqlrep.connect(silent=True))

    @mock.patch("mysql_class.Server.connect")
    def test_silent_false(self, mock_server):

        """Function:  test_silent_false

        Description:  Test with silent false set.

        Arguments:

        """

        mock_server.return_value = True

        self.assertFalse(self.mysqlrep.connect(silent=False))

    @mock.patch("mysql_class.Server.connect")
    def test_silent_default(self, mock_server):

        """Function:  test_silent_default

        Description:  Test with silent default setting.

        Arguments:

        """

        mock_server.return_value = True

        self.assertFalse(self.mysqlrep.connect())

    @mock.patch("mysql_class.SlaveRep.upd_slv_status")
    @mock.patch("mysql_class.Server.set_srv_gtid")
    @mock.patch("mysql_class.Server.connect")
    def test_db_up(self, mock_conn, mock_set, mock_update):

        """Function:  test_db_up

        Description:  Test with connection up.

        Arguments:

        """

        mock_conn.return_value = True
        mock_set.return_value = True
        mock_update.return_value = True

        self.mysqlrep.conn = True

        self.assertFalse(self.mysqlrep.connect())

    @mock.patch("mysql_class.Server.connect")
    def test_db_down(self, mock_server):

        """Function:  test_db_down

        Description:  Test with connection down.

        Arguments:

        """

        mock_server.return_value = True

        self.assertFalse(self.mysqlrep.connect())


if __name__ == "__main__":
    unittest.main()
