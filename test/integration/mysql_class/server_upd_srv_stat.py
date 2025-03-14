# Classification (U)

"""Program:  server_upd_srv_stat.py

    Description:  Integration testing of Server.upd_srv_stat in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_upd_srv_stat.py

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
        test_query_cache_size
        test_percentage_attr
        test_decision
        test_derived
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

    def test_query_cache_size(self):

        """Function:  test_query_cache_size

        Description:  Test using version setting.

        Arguments:

        """

        self.svr.upd_srv_stat()

        self.assertTrue(
            (self.svr.qry_cache >= 0 and self.svr.version[0] < 8) or
            (self.svr.qry_cache == 0 and self.svr.version[0] >= 8))

    def test_percentage_attr(self):

        """Function:  test_percentage_attr

        Description:  Test one of the percentage attributes.

        Arguments:

        """

        self.svr.upd_srv_stat()

        self.assertGreaterEqual(self.svr.prct_mem, 0)

    def test_decision(self):

        """Function:  test_decision

        Description:  Test with decision based attributes.

        Arguments:

        """

        self.svr.upd_srv_stat()

        if self.svr.tmp_tbl > self.svr.max_heap_tbl:
            tmp_tbl = self.svr.tmp_tbl

        else:
            tmp_tbl = self.svr.max_heap_tbl

        self.assertEqual(self.svr.tmp_tbl_size, tmp_tbl)

    def test_derived(self):

        """Function:  test_derived

        Description:  Test with derived attributes.

        Arguments:

        """

        self.svr.upd_srv_stat()

        self.assertGreaterEqual(self.svr.thr_mem, 0)

    def test_base(self):

        """Function:  test_base

        Description:  Test with base attributes.

        Arguments:

        """

        self.svr.upd_srv_stat()

        self.assertGreaterEqual(self.svr.max_conn, 0)


if __name__ == "__main__":
    unittest.main()
