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

    Methods:
        __init__ -> Class initialization.
        connect ->  Stub holder for mysql_class.SlaveRep.connect method. 

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.conn = True

    def connect(self):

        """Method:  upd_slv_status

        Description:  Stub holder for mysql_class.SlaveRep.connect method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_add_down_conn_false -> Test with add_down and conn set to false.
        test_add_down_false -> Test with add_down option set to false.
        test_add_down_true -> Test with add_down option set to true.
        test_create_slv_array -> Test create_slv_array function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.slave = SlaveRep()
        self.cfg_array = {"name": "name", "sid": "sid", "user": "user",
                          "passwd": "pswd", "serv_os": "Linux",
                          "host": "hostname", "port": 3306,
                          "cfg_file": "cfg_file"}

    @mock.patch("mysql_libs.mysql_class.SlaveRep")
    def test_add_down_conn_false(self, mock_rep):

        """Function:  test_add_down_conn_false

        Description:  Test with add_down and conn set to false.

        Arguments:

        """

        self.slave.conn = False
        mock_rep.return_value = self.slave
        slaves = mysql_libs.create_slv_array([self.cfg_array], add_down=False)

        self.assertEqual(len(slaves), 0)

    @mock.patch("mysql_libs.mysql_class.SlaveRep")
    def test_add_down_false(self, mock_rep):

        """Function:  test_add_down_false

        Description:  Test with add_down option set to false.

        Arguments:

        """

        mock_rep.return_value = self.slave
        slaves = mysql_libs.create_slv_array([self.cfg_array], add_down=False)

        self.assertEqual(len(slaves), 1)

    @mock.patch("mysql_libs.mysql_class.SlaveRep")
    def test_add_down_true(self, mock_rep):

        """Function:  test_add_down_true

        Description:  Test with add_down option set to true.

        Arguments:

        """

        mock_rep.return_value = self.slave
        slaves = mysql_libs.create_slv_array([self.cfg_array])

        self.assertEqual(len(slaves), 1)

    @mock.patch("mysql_libs.mysql_class.SlaveRep")
    def test_create_slv_array(self, mock_rep):

        """Function:  test_create_slv_array

        Description:  Test create_slv_array function.

        Arguments:

        """

        mock_rep.return_value = self.slave
        slaves = mysql_libs.create_slv_array([self.cfg_array])

        self.assertEqual(len(slaves), 1)


if __name__ == "__main__":
    unittest.main()
