# Classification (U)

"""Program:  show_slave_hosts.py

    Description:  Integration testing of show_slave_hosts in mysql_class.py.

    Usage:
        test/integration/mysql_class/show_slave_hosts.py

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
        test_show_master_stat2
        test_show_master_stat

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

    def test_show_master_stat2(self):

        """Function:  test_show_master_stat2

        Description:  Test show_master_stat function.

        Arguments:

        """

        data = mysql_class.show_slave_hosts(self.svr)

        if "Replica_UUID" in data[0]:
            self.assertTrue(data[0]["Replica_UUID"])

        else:
            self.assertTrue(data[0]["Slave_UUID"])

    def test_show_master_stat(self):

        """Function:  test_show_master_stat

        Description:  Test show_master_stat function.

        Arguments:

        """

        data = mysql_class.show_slave_hosts(self.svr)

        self.assertIsInstance(data, list)


if __name__ == "__main__":
    unittest.main()
