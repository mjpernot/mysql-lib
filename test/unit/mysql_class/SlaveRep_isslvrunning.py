#!/usr/bin/python
# Classification (U)

"""Program:  SlaveRep_isslvrunning.py

    Description:  Unit testing of SlaveRep.is_slv_running in mysql_class.py.

    Usage:
        test/unit/mysql_class/SlaveRep_isslvrunning.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mysql_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_slv_both_true -> Test with all attrs set to True.
        test_slv_two_true -> Test with two attrs set to True.
        test_slv_run_true -> Test with run set to True.
        test_slv_sql_true -> Test with slv_sql set to True.
        test_slv_io_true -> Test with slv_io set to True.
        test_default -> Test show_slv_state method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_pwd"
        self.machine = "Linux"
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

    def test_slv_all_true(self):

        """Function:  test_slv_all_true

        Description:  Test with all attrs set to True.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "Yes"
        mysqlrep.slv_io = "Yes"
        mysqlrep.run = "Yes"

        self.assertTrue(mysqlrep.is_slv_running())

    def test_slv_two_true(self):

        """Function:  test_slv_two_true

        Description:  Test with two attrs set to True.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "Yes"
        mysqlrep.slv_io = "Yes"
        mysqlrep.run = "No"

        self.assertFalse(mysqlrep.is_slv_running())

    def test_slv_run_true(self):

        """Function:  test_slv_run_true

        Description:  Test with run set to True.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "No"
        mysqlrep.slv_io = "No"
        mysqlrep.run = "Yes"

        self.assertFalse(mysqlrep.is_slv_running())

    def test_slv_sql_true(self):

        """Function:  test_slv_sql_true

        Description:  Test with slv_sql set to True.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "Yes"
        mysqlrep.slv_io = "No"
        mysqlrep.run = "No"

        self.assertFalse(mysqlrep.is_slv_running())

    def test_slv_io_true(self):

        """Function:  test_slv_io_true

        Description:  Test with slv_io set to True.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "No"
        mysqlrep.run = "No"
        mysqlrep.slv_io = "Yes"

        self.assertFalse(mysqlrep.is_slv_running())

    def test_default(self):

        """Function:  test_default

        Description:  Test show_slv_state method.

        Arguments:

        """

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.slv_sql = "No"
        mysqlrep.run = "No"
        mysqlrep.slv_io = "No"

        self.assertFalse(mysqlrep.is_slv_running())


if __name__ == "__main__":
    unittest.main()