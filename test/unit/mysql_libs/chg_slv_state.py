# Classification (U)

"""Program:  chg_slv_state.py

    Description:  Unit testing of chg_slv_state in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/chg_slv_state.py

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
import mysql_libs                           # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class Server():

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__
        stop_slave
        start_slave
        upd_slv_status

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

    def stop_slave(self):

        """Method:  stop_slave

        Description:  Stub holder for mysql_class.Rep.stop_slave method.

        Arguments:

        """

        return True

    def start_slave(self):

        """Method:  start_slave

        Description:  Stub holder for mysql_class.Rep.start_slave method.

        Arguments:

        """

        return True

    def upd_slv_status(self):

        """Method:  upd_slv_status

        Description:  Stub holder for mysql_class.Rep.upd_slv_status method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_stop_option
        test_start_option
        test_else_option

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_stop_option(self):

        """Function:  test_stop_option

        Description:  Test with stop option selected.

        Arguments:

        """

        self.assertFalse(mysql_libs.chg_slv_state([self.server], "stop"))

    def test_start_option(self):

        """Function:  test_start_option

        Description:  Test with start option selected.

        Arguments:

        """

        self.assertFalse(mysql_libs.chg_slv_state([self.server], "start"))

    def test_else_option(self):

        """Function:  test_else_option

        Description:  Test with other option selected.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.chg_slv_state([self.server], "other"))


if __name__ == "__main__":
    unittest.main()
