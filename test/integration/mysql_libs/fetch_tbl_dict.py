#!/usr/bin/python
# Classification (U)

"""Program:  fetch_tbl_dict.py

    Description:  Integration testing of fetch_tbl_dict in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/fetch_tbl_dict.py

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
import mysql_libs                           # pylint:disable=E0401,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_fetch_tbl_dict

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

    def test_fetch_tbl_dict(self):

        """Function:  test_fetch_tbl_dict

        Description:  Test fetch_tbl_dict function.

        Arguments:

        """

        key_name = "TABLE_NAME"
        data = mysql_libs.fetch_tbl_dict(self.svr, "mysql")

        if key_name not in list(data[0].keys()):
            key_name = "table_name"

        self.assertIn("db", [item[key_name] for item in data])


if __name__ == "__main__":
    unittest.main()
