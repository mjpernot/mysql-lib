# Classification (U)

"""Program:  slaverep_get_thr_stat.py

    Description:  Integration testing of SlaveRep.get_thr_stat in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/slaverep_get_thr_stat.py

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
        test_slv_sql
        test_slv_io
        test_io_state

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

    def test_run(self):

        """Function:  test_run

        Description:  Test with run attribute.

        Arguments:

        """

        data = self.svr.get_thr_stat()

        self.assertTrue(data[3])

    def test_slv_sql(self):

        """Function:  test_slv_sql

        Description:  Test with slv_sql attribute.

        Arguments:

        """

        data = self.svr.get_thr_stat()

        self.assertTrue(data[2])

    def test_slv_io(self):

        """Function:  test_slv_io

        Description:  Test with slv_io attribute.

        Arguments:

        """

        data = self.svr.get_thr_stat()

        self.assertTrue(data[1])

    def test_io_state(self):

        """Function:  test_io_state

        Description:  Test with io_state attribute.

        Arguments:

        """

        data = self.svr.get_thr_stat()

        self.assertTrue(data[0])


if __name__ == "__main__":
    unittest.main()
