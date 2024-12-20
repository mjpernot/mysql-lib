#!/usr/bin/python
# Classification (U)

"""Program:  create_slv_array.py

    Description:  Integration testing of create_slv_array in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/create_slv_array.py

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
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_create_slv_array2
        test_create_slv_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave.txt"

    def test_create_slv_array2(self):

        """Function:  test_create_slv_array2

        Description:  Test create_slv_array function.

        Arguments:

        """

        slaves = gen_libs.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        srv = mysql_libs.create_slv_array(slaves)

        self.assertIsInstance(srv[0], mysql_class.SlaveRep)

    def test_create_slv_array(self):

        """Function:  test_create_slv_array

        Description:  Test create_slv_array function.

        Arguments:

        """

        slaves = gen_libs.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        srv = mysql_libs.create_slv_array(slaves)

        self.assertIsInstance(srv, list)


if __name__ == "__main__":
    unittest.main()
