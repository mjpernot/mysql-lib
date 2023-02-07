# Classification (U)

"""Program:  rep_fetchdodb.py

    Description:  Unit testing of Rep.fetch_do_db in mysql_class.py.

    Usage:
        test/unit/mysql_class/rep_fetchdodb.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_class
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_list
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

    def test_list(self):

        """Function:  test_list

        Description:  Test fetch_do_db method with data.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(self.name, self.server_id, self.sql_user,
                                   self.sql_pass, self.machine,
                                   defaults_file=self.defaults_file)

        mysqlrep.do_db = "DB1,DB2,DB3"
        self.assertEqual(mysqlrep.fetch_do_db(), ["DB1", "DB2", "DB3"])

    def test_default(self):

        """Function:  test_default

        Description:  Test fetch_do_db method with no data.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(self.name, self.server_id, self.sql_user,
                                   self.sql_pass, self.machine,
                                   defaults_file=self.defaults_file)

        self.assertEqual(mysqlrep.fetch_do_db(), [])


if __name__ == "__main__":
    unittest.main()
