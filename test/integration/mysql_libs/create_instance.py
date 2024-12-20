#!/usr/bin/python
# Classification (U)

"""Program:  create_instance.py

    Description:  Integration testing of create_instance in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/create_instance.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_libs                           # pylint:disable=E0401,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_rep_user
        test_create_slv_rep_inst
        test_create_mst_rep_inst
        test_create_rep_inst
        test_create_server_inst

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mysql_cfg"
        self.rep_user = "REP_USER"

    def test_rep_user(self):

        """Function:  test_rep_user

        Description:  Test with passing rep_user information.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.SlaveRep)

        self.assertEqual(srv.rep_user, self.rep_user)

    def test_create_slv_rep_inst(self):

        """Function:  test_create_slv_rep_inst

        Description:  Test with SlaveRep class instance.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.SlaveRep)

        self.assertIsInstance(srv, mysql_class.SlaveRep)

    def test_create_mst_rep_inst(self):

        """Function:  test_create_mst_rep_inst

        Description:  Test with MasterRep class instance.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.MasterRep)

        self.assertIsInstance(srv, mysql_class.MasterRep)

    def test_create_rep_inst(self):

        """Function:  test_create_rep_inst

        Description:  Test with Rep class instance.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.Rep)

        self.assertIsInstance(srv, mysql_class.Rep)

    def test_create_server_inst(self):

        """Function:  test_create_server_inst

        Description:  Test with Server class instance.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.Server)

        self.assertIsInstance(srv, mysql_class.Server)


if __name__ == "__main__":
    unittest.main()
