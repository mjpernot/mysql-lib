# Classification (U)

"""Program:  slaverep_show_slv_state.py

    Description:  Integration testing of SlaveRep.show_slv_state in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/slaverep_show_slv_state.py

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
        test_down_slave
        test_up_slave
        tearDown

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

    def test_down_slave(self):

        """Function:  test_down_slave

        Description:  Test with stats with non-running slave.

        Arguments:

        """

        self.svr.stop_slave()
        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            self.assertTrue(self.status)

        else:
            data = self.svr.show_slv_state()

            self.assertEqual((data[0], data[1], data[2]), ("", "No", "No"))

    def test_up_slave(self):

        """Function:  test_up_slave

        Description:  Test with stats with running slave.

        Arguments:

        """

        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            data = self.svr.show_slv_state()

            self.assertEqual((data[1], data[2]), ("Yes", "Yes"))
            self.assertTrue(data[0])

        else:
            self.assertTrue(self.status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing environment.

        Arguments:

        """

        self.svr.start_slave()


if __name__ == "__main__":
    unittest.main()
