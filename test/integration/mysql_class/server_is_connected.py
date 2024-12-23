# Classification (U)

"""Program:  server_is_connected.py

    Description:  Integration testing of Server.is_connected in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_is_connected.py

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
        test_is_connected_true
        test_is_connected_false

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

    def test_is_connected_true(self):

        """Function:  test_is_connected_true

        Description:  Test is_connected is True.

        Arguments:

        """

        self.assertTrue(self.svr.is_connected())

    def test_is_connected_false(self):

        """Function:  test_is_connected_false

        Description:  Test is_connected is False.

        Arguments:

        """

        self.svr.disconnect()

        self.assertFalse(self.svr.is_connected())


if __name__ == "__main__":
    unittest.main()
