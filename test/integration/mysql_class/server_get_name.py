# Classification (U)

"""Program:  server_get_name.py

    Description:  Integration testing of Server.get_name in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_get_name.py

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
        test_get_name

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
        self.name = cfg.name

    def test_get_name(self):

        """Function:  test_get_name

        Description:  Test get_name method.

        Arguments:

        """

        self.assertEqual(self.svr.get_name(), self.name)


if __name__ == "__main__":
    unittest.main()
