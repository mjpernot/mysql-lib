# Classification (U)

"""Program:  server_cmd_sql.py

    Description:  Integration testing of Server.cmd_sql in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_cmd_sql.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_class
import lib.gen_libs as gen_libs
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_cmd_sql

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

    def test_cmd_sql(self):

        """Function:  test_cmd_sql

        Description:  Test with cmd_sql method.

        Arguments:

        """

        data = self.svr.cmd_sql(self.cmd)

        self.assertTrue(isinstance(data, dict))


if __name__ == "__main__":
    unittest.main()
