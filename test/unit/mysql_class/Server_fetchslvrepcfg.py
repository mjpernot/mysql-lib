#!/usr/bin/python
# Classification (U)

"""Program:  Server_fetchslvrepcfg.py

    Description:  Unit testing of Server.fetch_slv_rep_cfg in mysql_class.py.

    Usage:
        test/unit/mysql_class/Server_fetchslvrepcfg.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_value -> Test with values returned.

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

    def test_value(self):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        self.assertEqual(mysqldb.fetch_slv_rep_cfg(),
                         ({"log_bin": None, "sync_relay_log": None,
                           "read_only": None, "sync_master_info": None,
                           "log_slave_updates": None,
                           "sync_relay_log_info": None}))


if __name__ == "__main__":
    unittest.main()
