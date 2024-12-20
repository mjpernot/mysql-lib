# Classification (U)

"""Program:  fetch_sys_var.py

    Description:  Integration testing of fetch_sys_var in mysql_class.py.

    Usage:
        test/Integration/mysql_class/fetch_sys_var.py

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
        test_fetch_session
        test_fetch_default

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

    def test_fetch_global(self):

        """Function:  test_fetch_session

        Description:  Test with session level variable.

        Arguments:

        """

        data = mysql_class.fetch_sys_var(self.svr, "wait_timeout",
                                         level="global")
        self.assertGreaterEqual(int(data["wait_timeout"]), 0)

    def test_fetch_session(self):

        """Function:  test_fetch_session

        Description:  Test with session level variable.

        Arguments:

        """

        data = mysql_class.fetch_sys_var(self.svr, "warning_count",
                                         level="session")
        self.assertGreaterEqual(int(data["warning_count"]), 0)

    def test_fetch_default(self):

        """Function:  test_fetch_default

        Description:  Test with level variable.

        Arguments:

        """

        data = mysql_class.fetch_sys_var(self.svr, "warning_count")
        self.assertGreaterEqual(int(data["warning_count"]), 0)


if __name__ == "__main__":
    unittest.main()
