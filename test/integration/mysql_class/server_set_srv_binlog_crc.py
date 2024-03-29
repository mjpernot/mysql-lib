# Classification (U)

"""Program:  server_set_srv_binlog_crc.py

    Description:  Integration testing of Server.set_srv_binlog_crc in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/server_set_srv_binlog_crc.py

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
        test_value

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

    def test_value(self):

        """Function:  test_value

        Description:  Test with value returned.

        Arguments:

        """

        status = False

        self.svr.set_srv_binlog_crc()

        if self.svr.crc:
            status = True

        self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
