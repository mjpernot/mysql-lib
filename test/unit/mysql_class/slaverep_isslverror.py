# Classification (U)

"""Program:  slaverep_isslverror.py

    Description:  Unit testing of SlaveRep.is_slv_error in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_isslverror.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import lib.machine as machine               # pylint:disable=E0401,R0402,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_slv_both_true
        test_sql_err_true
        test_io_err_true
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

    def test_slv_both_true(self):

        """Function:  test_slv_both_true

        Description:  Test with all attrs set to True.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.sql_err = "Yes"
        mysqlrep.io_err = "Yes"

        self.assertTrue(mysqlrep.is_slv_error())

    def test_sql_err_true(self):

        """Function:  test_sql_err_true

        Description:  Test with sql_err set to True.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.sql_err = "Yes"
        mysqlrep.io_err = None

        self.assertTrue(mysqlrep.is_slv_error())

    def test_io_err_true(self):

        """Function:  test_io_err_true

        Description:  Test with io_err set to True.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.sql_err = None
        mysqlrep.io_err = "Yes"

        self.assertTrue(mysqlrep.is_slv_error())

    def test_default(self):

        """Function:  test_default

        Description:  Test is_slv_error method.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.sql_err = None
        mysqlrep.io_err = None

        self.assertFalse(mysqlrep.is_slv_error())


if __name__ == "__main__":
    unittest.main()
