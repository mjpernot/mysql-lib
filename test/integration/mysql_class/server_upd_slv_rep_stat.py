# Classification (U)

"""Program:  server_upd_slv_rep_stat.py

    Description:  Integration testing of Server.upd_slv_rep_stat in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/server_upd_slv_rep_stat.py

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
        test_sync_rly_info
        test_sync_relay
        test_sync_mst
        test_log_slv_upd
        test_read_only
        test_log_bin

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "master_mysql_cfg"
        cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.MasterRep(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.svr.connect()

    def test_sync_rly_info(self):

        """Function:  test_sync_rly_info

        Description:  Test the sync_rly_info is set.

        Arguments:

        """

        self.svr.upd_slv_rep_stat()

        self.assertTrue(self.svr.sync_rly_info)

    def test_sync_relay(self):

        """Function:  test_sync_relay

        Description:  Test the sync_relay is set.

        Arguments:

        """

        self.svr.upd_slv_rep_stat()

        self.assertTrue(self.svr.sync_relay)

    def test_sync_mst(self):

        """Function:  test_sync_mst

        Description:  Test the sync_mst is set.

        Arguments:

        """

        self.svr.upd_slv_rep_stat()

        self.assertTrue(self.svr.sync_mst)

    def test_log_slv_upd(self):

        """Function:  test_log_slv_upd

        Description:  Test the log_slv_upd is set.

        Arguments:

        """

        self.svr.upd_slv_rep_stat()

        self.assertTrue(self.svr.log_slv_upd)

    def test_read_only(self):

        """Function:  test_read_only

        Description:  Test the read_only is set.

        Arguments:

        """

        self.svr.upd_slv_rep_stat()

        self.assertTrue(self.svr.read_only)

    def test_log_bin(self):

        """Function:  test_log_bin

        Description:  Test the log_bin is set.

        Arguments:

        """

        self.svr.upd_slv_rep_stat()

        self.assertTrue(self.svr.log_bin)


if __name__ == "__main__":
    unittest.main()
