# Classification (U)

"""Program:  server_flushlogs.py

    Description:  Unit testing of Server.flush_logs in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_flushlogs.py

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
        test_flush_logs

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

    @mock.patch("mysql_class.Server.upd_log_stats")
    @mock.patch("mysql_class.flush_logs")
    def test_flush_logs(self, mock_logs, mock_update):

        """Function:  test_flush_logs

        Description:  Test flush_logs method.

        Arguments:

        """

        mock_logs.return_value = True
        mock_update.return_value = True
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.flush_logs())


if __name__ == "__main__":
    unittest.main()
