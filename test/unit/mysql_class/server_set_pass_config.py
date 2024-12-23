# Classification (U)

"""Program:  server_set_pass_config.py

    Description:  Unit testing of Server.set_pass_config method in
        mysql_class.py.

    Usage:
        test/unit/mysql_class/server_set_pass_config.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import lib.machine as machine               # pylint:disable=E0401,R0402,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__

# Global


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_change_pass
        test_set_pass_config

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
        self.new_sql_pass = "my_japd2"

    def test_change_pass(self):

        """Function:  test_change_pass

        Description:  Test change passwd and update config.

        Arguments:

        """

        new_config = {"passwd": self.new_sql_pass}

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)
        mysqldb.sql_pass = self.new_sql_pass
        mysqldb.set_pass_config()

        self.assertEqual((mysqldb.config, mysqldb.sql_pass),
                         (new_config, self.new_sql_pass))

    def test_set_pass_config(self):

        """Function:  test_set_pass_config

        Description:  Test setting configuration settings.

        Arguments:

        """

        config = {"passwd": self.sql_pass}

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

        self.assertEqual(mysqldb.config, config)


if __name__ == "__main__":
    unittest.main()
