# Classification (U)

"""Program:  server_fetchmstrepcfg.py

    Description:  Unit testing of Server.fetch_mst_rep_cfg in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_fetchmstrepcfg.py

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

    def test_value(self):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        self.assertEqual(mysqldb.fetch_mst_rep_cfg(),
                         ({"log_bin": None, "innodb_support_xa": None,
                           "sync_binlog": None, "binlog_format": None,
                           "innodb_flush_log_at_trx_commit": None}))


if __name__ == "__main__":
    unittest.main()
