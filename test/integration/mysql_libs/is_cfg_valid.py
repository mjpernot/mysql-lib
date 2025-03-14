#!/usr/bin/python
# Classification (U)

"""Program:  is_cfg_valid.py

    Description:  Integration testing of is_cfg_valid in mysql_libs.py.

    Note:  This assumes the extra_def_file setting was set.

    Usage:
        test/integration/mysql_libs/is_cfg_valid.py

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
        test_multi_both_fail
        test_multi_one_fail
        test_multi_servers
        test_chk_fails
        test_cfg_valid

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
            port=cfg.port, defaults_file=cfg.cfg_file,
            extra_def_file=cfg.extra_def_file)
        self.svr2 = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.msg = [self.svr2.name + ":  extra_def_file is not set."]
        self.svr3 = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file,
            extra_def_file=cfg.extra_def_file)
        self.svr4 = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.msg2 = list(self.msg)
        self.msg2.append(self.svr4.name + ":  extra_def_file is not set.")

    def test_multi_both_fail(self):

        """Function:  test_multi_both_fail

        Description:  Test with multiple servers with both failed.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr2, self.svr4]),
                         (False, self.msg2))

    def test_multi_one_fail(self):

        """Function:  test_multi_one_fail

        Description:  Test with multiple servers with one failed.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr, self.svr2]),
                         (False, self.msg))

    def test_multi_servers(self):

        """Function:  test_multi_servers

        Description:  Test with multiple servers valid.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr, self.svr3]),
                         (True, []))

    def test_chk_fails(self):

        """Function:  test_chk_fails

        Description:  Test with check file fails.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr2]),
                         (False, self.msg))

    def test_cfg_valid(self):

        """Function:  test_cfg_valid

        Description:  Test with extra cfg file is valid.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr]), (True, []))


if __name__ == "__main__":
    unittest.main()
