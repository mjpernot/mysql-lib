# Classification (U)

"""Program:  server_fetch_log.py

    Description:  Integration testing of Server.fetch_log in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/server_fetch_log.py

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
        test_no_file
        test_base

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

    def test_no_file(self):

        """Function:  test_no_file

        Description:  Test with no file updated.

        Arguments:

        """

        self.svr.fetch_log()

        self.assertTrue(self.svr.file)

    def test_base(self):

        """Function:  test_base

        Description:  Test with base attribute.

        Arguments:

        """

        self.svr.upd_log_stats()
        fname = self.svr.file
        self.svr.fetch_log()

        self.assertEqual(self.svr.file, fname)


if __name__ == "__main__":
    unittest.main()
