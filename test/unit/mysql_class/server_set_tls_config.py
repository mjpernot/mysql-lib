# Classification (U)

"""Program:  server_set_tls_config.py

    Description:  Unit testing of Server.set_tls_config in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_set_tls_config.py

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
        test_tls_non_list2
        test_tls_non_list
        test_tls_list2
        test_tls_list
        test_tls_version2
        test_tls_version

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        tls12 = "TLSv1.2"
        key1 = "pass"
        key2 = "wd"
        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3306
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"
        self.tls_versions = ["TLSv1.1", tls12]
        self.tls_versions2 = tls12
        self.tls_versions2a = [tls12]

        self.config = {}
        self.config[key1 + key2] = self.sql_pass

        self.config2 = {}
        self.config2[key1 + key2] = self.sql_pass
        self.config2["tls_versions"] = self.tls_versions

        self.config3 = {}
        self.config3[key1 + key2] = self.sql_pass
        self.config3["tls_versions"] = self.tls_versions2a

    def test_tls_non_list2(self):

        """Function:  test_tls_non_list2

        Description:  Test with tls_version string passed.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, tls_versions=self.tls_versions2)

        self.assertEqual(mysqldb.config, self.config3)

    def test_tls_non_list(self):

        """Function:  test_tls_non_list

        Description:  Test with tls_version string passed.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, tls_versions=self.tls_versions2)

        self.assertEqual(mysqldb.tls_versions, self.tls_versions2)

    def test_tls_list2(self):

        """Function:  test_tls_list2

        Description:  Test with tls_version list passed.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, tls_versions=self.tls_versions)

        self.assertEqual(mysqldb.config, self.config2)

    def test_tls_list(self):

        """Function:  test_tls_list

        Description:  Test with tls_version list passed.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, tls_versions=self.tls_versions)

        self.assertEqual(mysqldb.tls_versions, self.tls_versions)

    def test_tls_version2(self):

        """Function:  test_tls_version2

        Description:  Test with default tls_version setting.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.config, self.config)

    def test_tls_version(self):

        """Function:  test_tls_version

        Description:  Test with default tls_version setting.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.tls_versions, [])


if __name__ == "__main__":
    unittest.main()
