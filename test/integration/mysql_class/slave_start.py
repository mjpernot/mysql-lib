# Classification (U)

"""Program:  slave_start.py

    Description:  Integration testing of slave_start in mysql_class.py.

    Usage:
        test/integration/mysql_class/slave_start.py

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
        test_started_slave
        test_start_slave

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave_mysql_cfg"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.SlaveRep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)
        self.svr.connect()
        self.status = False

    def test_started_slave(self):

        """Function:  test_started_slave

        Description:  Test with slave already up.

        Arguments:

        """

        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            mysql_class.slave_start(self.svr)
            self.svr.upd_slv_status()

            self.assertTrue(self.svr.is_slv_running())

        else:
            self.assertTrue(self.status)

    def test_start_slave(self):

        """Function:  test_start_slave

        Description:  Test with starting running slave.

        Arguments:

        """

        self.svr.stop_slave()
        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            self.assertTrue(self.status)

        else:
            mysql_class.slave_start(self.svr)
            self.svr.upd_slv_status()

            self.assertTrue(self.svr.is_slv_running())


if __name__ == "__main__":
    unittest.main()
