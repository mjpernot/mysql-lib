# Classification (U)

"""Program:  server_col_sql.py

    Description:  Integration testing of Server.col_sql in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_col_sql.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import lib.gen_libs as gen_libs             # pylint:disable=E0401,R0402,C0413
import lib.machine as machine               # pylint:disable=E0401,R0402,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_col_sql2
        test_col_sql

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mysql_cfg"
        cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.svr.connect()
        self.cmd = "show databases"
        self.database = "mysql"

    def test_col_sql2(self):

        """Function:  test_col_sql2

        Description:  Test with col_sql method.

        Arguments:

        """

        data = self.svr.col_sql(self.cmd)

        self.assertIsInstance(data, list)

    def test_col_sql(self):

        """Function:  test_col_sql

        Description:  Test with col_sql method.

        Arguments:

        """

        data = self.svr.col_sql(self.cmd)
        db_list = []

        for item in data:
            db_list.append(item["Database"])

        self.assertIn(self.database, db_list)


if __name__ == "__main__":
    unittest.main()
