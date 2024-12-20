#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_create_instance.py

    Description:  Integration testing of create_instance in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/slaverep_create_instance.py

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
        test_create_instance

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave_mysql_cfg"

    def test_create_instance(self):

        """Function:  test_create_instance

        Description:  Test create_instance function.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.SlaveRep)

        self.assertIsInstance(srv, mysql_class.SlaveRep)


if __name__ == "__main__":
    unittest.main()
