# Classification (U)

"""Program:  rep_init.py

    Description:  Unit testing of Rep.__init__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/rep_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mysql.connector

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
        test_ssl_config7
        test_ssl_config6
        test_ssl_config5
        test_ssl_config4
        test_ssl_config3
        test_ssl_config2
        test_ssl_config
        test_ssl_verify_cert2
        test_ssl_verify_cert
        test_ssl_verify_id2
        test_ssl_verify_id
        test_ssl_disabled2
        test_ssl_disabled
        test_ssl_client_flag2
        test_ssl_client_flag
        test_ssl_client_cert2
        test_ssl_client_cert
        test_ssl_client_key2
        test_ssl_client_key
        test_ssl_client_ca2
        test_ssl_client_ca
        test_sql_pass
        test_indb_buf_write
        test_version
        test_config
        test_no_extra_def_file
        test_extra_def_file
        test_no_port
        test_port
        test_no_host
        test_host
        test_no_default
        test_default
        test_min

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        key1 = "pass"
        key2 = "wd"
        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"
        self.results = self.machine.defaults_file

        self.config = {}
        self.config[key1 + key2] = self.sql_pass

        self.config2 = {}
        self.config2[key1 + key2] = self.sql_pass
        self.config2["ssl_ca"] = "CAFile"
        self.config2["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config2["ssl_disabled"] = False
        self.config2["ssl_verify_identity"] = False
        self.config2["ssl_verify_cert"] = False

        self.config3 = {}
        self.config3[key1 + key2] = self.sql_pass
        self.config3["ssl_key"] = "KeyFile"
        self.config3["ssl_cert"] = "CertFile"
        self.config3["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config3["ssl_ca"] = ""
        self.config3["ssl_disabled"] = False
        self.config3["ssl_verify_identity"] = False

        self.config4 = {}
        self.config4[key1 + key2] = self.sql_pass
        self.config4["ssl_ca"] = "CAFile"
        self.config4["ssl_key"] = "KeyFile"
        self.config4["ssl_cert"] = "CertFile"
        self.config4["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config4["ssl_disabled"] = False
        self.config4["ssl_verify_identity"] = False
        self.config4["ssl_verify_cert"] = False

        self.config5 = {}
        self.config5[key1 + key2] = self.sql_pass
        self.config5["ssl_ca"] = "CAFile"
        self.config5["ssl_key"] = "KeyFile"
        self.config5["ssl_cert"] = "CertFile"
        self.config5["client_flags"] = [4096]
        self.config5["ssl_disabled"] = False
        self.config5["ssl_verify_identity"] = False
        self.config5["ssl_verify_cert"] = False

        self.config6 = {}
        self.config6[key1 + key2] = self.sql_pass
        self.config6["ssl_ca"] = "CAFile"
        self.config6["ssl_key"] = "KeyFile"
        self.config6["ssl_cert"] = "CertFile"
        self.config6["client_flags"] = [4096]
        self.config6["ssl_disabled"] = True
        self.config6["ssl_verify_identity"] = False
        self.config6["ssl_verify_cert"] = False

        self.config7 = {}
        self.config7[key1 + key2] = self.sql_pass
        self.config7["ssl_ca"] = "CAFile"
        self.config7["ssl_key"] = "KeyFile"
        self.config7["ssl_cert"] = "CertFile"
        self.config7["client_flags"] = [4096]
        self.config7["ssl_disabled"] = False
        self.config7["ssl_verify_identity"] = True
        self.config7["ssl_verify_cert"] = False

        self.config8 = {}
        self.config8[key1 + key2] = self.sql_pass
        self.config8["ssl_ca"] = "CAFile"
        self.config8["ssl_key"] = "KeyFile"
        self.config8["ssl_cert"] = "CertFile"
        self.config8["client_flags"] = [4096]
        self.config8["ssl_disabled"] = False
        self.config8["ssl_verify_identity"] = False
        self.config8["ssl_verify_cert"] = True

    def test_ssl_config7(self):

        """Function:  test_ssl_config7

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile",
            ssl_client_flag=4096, ssl_verify_cert=True)

        self.assertEqual(mysqlrep.config, self.config8)

    def test_ssl_config6(self):

        """Function:  test_ssl_config6

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile",
            ssl_client_flag=4096, ssl_verify_id=True)

        self.assertEqual(mysqlrep.config, self.config7)

    def test_ssl_config5(self):

        """Function:  test_ssl_config5

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile",
            ssl_client_flag=4096, ssl_disabled=True)

        self.assertEqual(mysqlrep.config, self.config6)

    def test_ssl_config4(self):

        """Function:  test_ssl_config4

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile",
            ssl_client_flag=4096)

        self.assertEqual(mysqlrep.config, self.config5)

    def test_ssl_config3(self):

        """Function:  test_ssl_config3

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile")

        self.assertEqual(mysqlrep.config, self.config4)

    def test_ssl_config2(self):

        """Function:  test_ssl_config2

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key="KeyFile",
            ssl_client_cert="CertFile")

        self.assertEqual(mysqlrep.config, self.config3)

    def test_ssl_config(self):

        """Function:  test_ssl_config

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile")

        self.assertEqual(mysqlrep.config, self.config2)

    def test_ssl_verify_cert2(self):

        """Function:  test_ssl_verify_cert2

        Description:  Test with ssl_verify_cert attribute.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_verify_cert=True)

        self.assertTrue(mysqldb.ssl_verify_cert)

    def test_ssl_verify_cert(self):

        """Function:  test_ssl_verify_cert

        Description:  Test with ssl_verify_cert attribute.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertFalse(mysqldb.ssl_verify_cert)

    def test_ssl_verify_id2(self):

        """Function:  test_ssl_verify_id2

        Description:  Test with ssl_verify_id attribute.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_verify_id=True)

        self.assertTrue(mysqldb.ssl_verify_id)

    def test_ssl_verify_id(self):

        """Function:  test_ssl_verify_id

        Description:  Test with ssl_verify_id attribute.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertFalse(mysqldb.ssl_verify_id)

    def test_ssl_disabled2(self):

        """Function:  test_ssl_disabled2

        Description:  Test with ssl_disabled attribute.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_disabled=True)

        self.assertTrue(mysqldb.ssl_disabled)

    def test_ssl_disabled(self):

        """Function:  test_ssl_disabled

        Description:  Test with ssl_disabled attribute.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertFalse(mysqldb.ssl_disabled)

    def test_ssl_client_flag2(self):

        """Function:  test_ssl_client_flag2

        Description:  Test with ssl_client_flag attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_flag=4096)

        self.assertEqual(mysqlrep.ssl_client_flag, 4096)

    def test_ssl_client_flag(self):

        """Function:  test_ssl_client_flag

        Description:  Test with ssl_client_flag attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqlrep.ssl_client_flag,
                         mysql.connector.ClientFlag.SSL)

    def test_ssl_client_cert2(self):

        """Function:  test_ssl_client_cert2

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_cert="CertFile")

        self.assertEqual(mysqlrep.ssl_client_cert, "CertFile")

    def test_ssl_client_cert(self):

        """Function:  test_ssl_client_cert

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertIsNone(mysqlrep.ssl_client_cert)

    def test_ssl_client_key2(self):

        """Function:  test_ssl_client_key2

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key="KeyFile")

        self.assertEqual(mysqlrep.ssl_client_key, "KeyFile")

    def test_ssl_client_key(self):

        """Function:  test_ssl_client_key

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertIsNone(mysqlrep.ssl_client_key)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_ca2

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile")

        self.assertEqual(mysqlrep.ssl_client_ca, "CAFile")

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_ca

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertIsNone(mysqlrep.ssl_client_ca)

    def test_sql_pass(self):

        """Function:  test_sql_pass

        Description:  Test with sql_pass attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqlrep.sql_pass, self.sql_pass)

    def test_indb_buf_write(self):

        """Function:  test_indb_buf_write

        Description:  Test with indb_buf_write attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertIsNone(mysqlrep.indb_buf_write)

    def test_version(self):

        """Function:  test_version

        Description:  Test with version attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertIsNone(mysqlrep.version)

    def test_config(self):

        """Function:  test_config

        Description:  Test with config attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port, mysqlrep.config),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306, self.config))

    def test_no_extra_def_file(self):

        """Function:  test_no_extra_def_file

        Description:  Test with no extra_def_file arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port, mysqlrep.extra_def_file),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306, None))

    def test_extra_def_file(self):

        """Function:  test_extra_def_file

        Description:  Test with passing extra_def_file arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, extra_def_file=self.extra_def_file)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port, mysqlrep.extra_def_file),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306, self.extra_def_file))

    def test_no_port(self):

        """Function:  test_no_port

        Description:  Test with no port arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqlrep.port, 3306)

    def test_port(self):

        """Function:  test_port

        Description:  Test with passing port arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, port=self.port)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", self.port))

    def test_no_host(self):

        """Function:  test_no_host

        Description:  Test with no host arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqlrep.host, "localhost")

    def test_host(self):

        """Function:  test_host

        Description:  Test with passing host arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, host=self.host)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, self.host, 3306))

    def test_no_default(self):

        """Function:  test_no_default

        Description:  Test with no default file.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqlrep.defaults_file, self.results)

    def test_default(self):

        """Function:  test_default

        Description:  Test with default file.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306))

    def test_min(self):

        """Function:  test_min

        Description:  Test with minimum number of arguments.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306))


if __name__ == "__main__":
    unittest.main()
