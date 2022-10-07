# Classification (U)

"""Program:  rep_verify_srv_id.py

    Description:  Unit testing of Rep.verify_srv_id method in Rep class in
        mysql_class.py.

    Usage:
        test/unit/mysql_class/rep_verify_srv_id.py

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
import mysql_class
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ids_not_match
        test_ids_match

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

    @mock.patch("mysql_class.fetch_sys_var")
    def test_ids_not_match(self, mock_fetch):

        """Function:  test_ids_not_match

        Description:  Test server and config ids do not match.

        Arguments:

        """

        mock_fetch.return_value = {"server_id": 11}
        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqlrep.verify_srv_id())

    @mock.patch("mysql_class.fetch_sys_var")
    def test_ids_match(self, mock_fetch):

        """Function:  test_ids_match

        Description:  Test server and config ids match.

        Arguments:

        """

        mock_fetch.return_value = {"server_id": 10}
        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertTrue(mysqlrep.verify_srv_id())


if __name__ == "__main__":
    unittest.main()
