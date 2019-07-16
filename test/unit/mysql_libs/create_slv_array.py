#!/usr/bin/python
# Classification (U)

"""Program:  create_slv_array.py

    Description:  Unit testing of create_slv_array in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/create_slv_array.py

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
import mock

# Local
sys.path.append(os.getcwd())
import mysql_libs
import version

__version__ = version.__version__


class SlaveRep(object):

    """Class:  SlaveRep

    Description:  Class stub holder for mysql_class.SlaveRep class.

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.
        connect ->  Stub holder for mysql_class.SlaveRep.connect method. 

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def connect(self):

        """Method:  upd_slv_status

        Description:  Stub holder for mysql_class.SlaveRep.connect method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_create_slv_array -> Test create_slv_array function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.slave = SlaveRep()
        self.cfg_array = {"name": "name", "sid": "sid", "user": "user",
                          "passwd": "pwd", "serv_os": "Linux",
                          "host": "hostname", "port": 3306,
                          "cfg_file": "cfg_file"}

    @mock.patch("mysql_libs.mysql_class.SlaveRep")
    def test_create_slv_array(self, mock_rep):

        """Function:  test_create_slv_array

        Description:  Test create_slv_array function.

        Arguments:

        """

        mock_rep.return_value = self.slave
        slaves = mysql_libs.create_slv_array([self.cfg_array])

        self.assertEqual(len(slaves), 1)
#        self.assertEqual(mysql_libs.create_slv_array([self.cfg_array]),
#                         ["Rep_Instance"])


if __name__ == "__main__":
    unittest.main()
