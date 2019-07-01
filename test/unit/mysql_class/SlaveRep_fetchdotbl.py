#!/usr/bin/python
# Classification (U)

"""Program:  SlaveRep_fetchdotbl.py

    Description:  Unit testing of SlaveRep.fetch_do_tbl in mysql_class.py.

    Usage:
        test/unit/mysql_class/SlaveRep_fetchdotbl.py

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
        test_list -> Test fetch_do_tbl method with data.
        test_default -> Test fetch_do_tbl method with no data.

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

    def test_list(self):

        """Function:  test_list

        Description:  Test fetch_do_tbl method with data.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(self.name, self.server_id, self.sql_user,
                                   self.sql_pass, self.machine,
                                   defaults_file=self.defaults_file)

        mysqlrep.do_dic = "Tbl1, Tbl2, Tbl3"
        self.assertEqual(mysqlrep.fetch_do_tbl(), ["Tbl1, Tbl2, Tbl3"])

    def test_default(self):

        """Function:  test_default

        Description:  Test fetch_do_tbl method with no data.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(self.name, self.server_id, self.sql_user,
                                   self.sql_pass, self.machine,
                                   defaults_file=self.defaults_file)

        self.assertEqual(mysqlrep.fetch_do_tbl(), [])


if __name__ == "__main__":
    unittest.main()
