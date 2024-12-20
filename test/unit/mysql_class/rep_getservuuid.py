# Classification (U)

"""Program:  rep_getservuuid.py

    Description:  Unit testing of Rep.get_serv_uuid in mysql_class.py.

    Usage:
        test/unit/mysql_class/rep_getservuuid.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import lib.machine as machine               # pylint:disable=E0401,R0402,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.server_uuid = "7d30665d-e05b-11ee-b514-ed1cc37dsa5a"
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

    @mock.patch("mysql_class.fetch_sys_var")
    def test_default(self, mock_fetch):

        """Function:  test_default

        Description:  Test get_serv_uuid method.

        Arguments:

        """

        mock_fetch.return_value = {"server_uuid": self.server_uuid}
        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        self.assertEqual(mysqlrep.get_serv_uuid(), self.server_uuid)


if __name__ == "__main__":
    unittest.main()
