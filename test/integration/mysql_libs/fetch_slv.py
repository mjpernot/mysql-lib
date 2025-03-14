#!/usr/bin/python
# Classification (U)

"""Program:  fetch_slv.py

    Description:  Integration testing of fetch_slv in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/fetch_slv.py

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
        test_not_found2
        test_not_found
        test_found2
        test_found

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave.txt"
        self.name = "NotFoundSlave"
        self.err_msg = \
            f"Error:  Slave {self.name} was not found in slave array."

    def test_not_found2(self):

        """Function:  test_not_found2

        Description:  Test with slave not found.

        Arguments:

        """

        slaves = gen_libs.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        servers = mysql_libs.create_slv_array(slaves)
        _, err_flag, err_msg = mysql_libs.fetch_slv(servers, self.name)

        self.assertEqual((err_flag, err_msg), (True, self.err_msg))

    def test_not_found(self):

        """Function:  test_not_found

        Description:  Test with slave not found.

        Arguments:

        """

        slaves = gen_libs.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        servers = mysql_libs.create_slv_array(slaves)
        slv, _, _ = mysql_libs.fetch_slv(servers, self.name)

        self.assertFalse(slv)

    def test_found2(self):

        """Function:  test_found2

        Description:  Test with slave found.

        Arguments:

        """

        slaves = gen_libs.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        name = slaves[0]["name"]
        servers = mysql_libs.create_slv_array(slaves)
        _, err_flag, err_msg = mysql_libs.fetch_slv(servers, name)

        self.assertEqual((err_flag, err_msg), (False, None))

    def test_found(self):

        """Function:  test_found

        Description:  Test with slave found.

        Arguments:

        """

        slaves = gen_libs.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        name = slaves[0]["name"]
        servers = mysql_libs.create_slv_array(slaves)
        slv, _, _ = mysql_libs.fetch_slv(servers, name)

        self.assertIsInstance(slv, mysql_class.SlaveRep)


if __name__ == "__main__":
    unittest.main()
