# Classification (U)

"""Program:  slaverep_upd_slv_status.py

    Description:  Integration testing of SlaveRep.upd_slv_status in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/slaverep_upd_slv_status.py

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
        test_run
        test_tran_retry
        test_conn_retry
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

    def test_run(self):

        """Function:  test_run

        Description:  Test with run attribute.

        Arguments:

        """

        self.svr.start_slave()

        if self.svr.is_slv_running():
            self.svr.upd_slv_status()

            self.assertTrue(self.svr.run)

        else:
            self.assertTrue(self.status)

    def test_tran_retry(self):

        """Function:  test_tran_retry

        Description:  Test with tran_retry attribute.

        Arguments:

        """

        self.svr.start_slave()

        if self.svr.is_slv_running():
            self.svr.upd_slv_status()

            self.assertTrue(self.svr.tran_retry)

        else:
            self.assertTrue(self.status)

    def test_conn_retry(self):

        """Function:  test_conn_retry

        Description:  Test with conn_retry attribute.

        Arguments:

        """

        self.svr.start_slave()

        if self.svr.is_slv_running():
            self.svr.upd_slv_status()

            self.assertTrue(self.svr.conn_retry)

        else:
            self.assertTrue(self.status)

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
            self.svr.upd_slv_status()

            self.assertEqual(
                (self.svr.io_state, self.svr.slv_io, self.svr.slv_sql),
                ("", "No", "No"))

    def test_up_slave(self):

        """Function:  test_up_slave

        Description:  Test with stats with running slave.

        Arguments:

        """

        self.svr.start_slave()

        if self.svr.is_slv_running():
            self.svr.upd_slv_status()

            self.assertEqual((self.svr.slv_io, self.svr.slv_sql),
                             ("Yes", "Yes"))
            self.assertTrue(self.svr.io_state)

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
