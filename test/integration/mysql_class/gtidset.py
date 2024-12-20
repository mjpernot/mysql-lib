# Classification (U)

"""Program:  gtidset.py

    Description:  Integration testing of GTIDSet class in mysql_class.py.

    Usage:
        test/integration/mysql_class/gtidset.py

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
        test_greater_than
        test_less_than
        test_not_equal
        test_greater_than_equal
        test_less_than_equal
        test_equal
        test_string2
        test_string
        test_is_class

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
        self.svr2 = mysql_class.SlaveRep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)
        self.svr2.connect()

    def test_greater_than(self):

        """Function:  test_greater_than

        Description:  Test with GTIDSets greater than.

        Arguments:

        """

        self.assertGreater(self.svr.exe_gtidset, self.svr2.exe_gtidset)

    def test_less_than(self):

        """Function:  test_less_than

        Description:  Test with GTIDSets less than.

        Arguments:

        """

        self.assertLess(self.svr.exe_gtidset, self.svr2.exe_gtidset)

    def test_not_equal(self):

        """Function:  test_not_equal

        Description:  Test with GTIDSets not equal.

        Arguments:

        """

        self.assertNotEqual(self.svr.exe_gtidset, self.svr2.exe_gtidset)

    def test_greater_than_equal(self):

        """Function:  test_greater_than_equal

        Description:  Test with GTIDSets greater than equal.

        Arguments:

        """

        self.assertGreaterEqual(self.svr.exe_gtidset, self.svr2.exe_gtidset)

    def test_less_than_equal(self):

        """Function:  test_less_than_equal

        Description:  Test with GTIDSets less than equal.

        Arguments:

        """

        self.assertLessEqual(self.svr.exe_gtidset, self.svr2.exe_gtidset)

    def test_equal(self):

        """Function:  test_equal

        Description:  Test with GTIDSets equal.

        Arguments:

        """

        self.assertEqual(self.svr.exe_gtidset, self.svr2.exe_gtidset)

    def test_string2(self):

        """Function:  test_string2

        Description:  Test conversion of GTIDSet to string.

        Arguments:

        """

        line = f"{self.svr.exe_gtidset}"

        self.assertIsInstance(line, str)

    def test_string(self):

        """Function:  test_string

        Description:  Test conversion of GTIDSet to string.

        Arguments:

        """

        line = str(self.svr.exe_gtidset)

        self.assertIsInstance(line, str)

    def test_is_class(self):

        """Function:  test_is_class

        Description:  Test is GTIDSets class.

        Arguments:

        """

        self.assertIsInstance(self.svr.exe_gtidset, mysql_class.GTIDSet)


if __name__ == "__main__":
    unittest.main()
