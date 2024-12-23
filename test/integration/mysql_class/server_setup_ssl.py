# Classification (U)

"""Program:  server_setup_ssl.py

    Description:  Integration testing of Server.setup_ssl in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_setup_ssl.py

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
import lib.gen_libs as gen_libs             # pylint:disable=E0401,R0402,C0413
import lib.machine as machine               # pylint:disable=E0401,R0402,C0413
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_key_cert_yes_ca3
        test_key_cert_yes_ca2
        test_key_cert_yes_ca
        test_key_cert_no_ca3
        test_key_cert_no_ca2
        test_key_cert_no_ca
        test_ssl_all2
        test_ssl_all
        test_ssl_client_cert
        test_ssl_client_key
        test_ssl_client_flag
        test_ssl_client_key_cert3
        test_ssl_client_key_cert2
        test_ssl_client_key_cert
        test_ssl_client_ca3
        test_ssl_client_ca2
        test_ssl_client_ca

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        key1 = "pass"
        key2 = "wd"
        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mysql_cfg"
        cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)

        self.ssl_client_ca = "CAFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_flag = mysql.connector.ClientFlag.SSL

        self.config = {}
        self.config[key1 + key2] = self.svr.sql_pass
        self.config["ssl_ca"] = "CAFile"
        self.config["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config["ssl_disabled"] = False
        self.config["ssl_verify_identity"] = False
        self.config["ssl_verify_cert"] = False

        self.config2 = {}
        self.config2[key1 + key2] = self.svr.sql_pass
        self.config2["ssl_key"] = "KeyFile"
        self.config2["ssl_cert"] = "CertFile"
        self.config2["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config2["ssl_ca"] = ""
        self.config2["ssl_disabled"] = False
        self.config2["ssl_verify_identity"] = False

        self.config3 = {}
        self.config3[key1 + key2] = self.svr.sql_pass
        self.config3["ssl_ca"] = "CAFile"
        self.config3["ssl_key"] = "KeyFile"
        self.config3["ssl_cert"] = "CertFile"
        self.config3["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config3["ssl_disabled"] = False
        self.config3["ssl_verify_identity"] = False
        self.config3["ssl_verify_cert"] = False

    def test_key_cert_yes_ca3(self):

        """Function:  test_key_cert_yes_ca3

        Description:  Test with cert and key present and with ca.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(self.svr.config, self.config3)

    def test_key_cert_yes_ca2(self):

        """Function:  test_key_cert_yes_ca2

        Description:  Test with cert and key present and with ca.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (self.svr.ssl_client_ca, self.svr.ssl_client_flag),
            (self.ssl_client_ca, mysql.connector.ClientFlag.SSL))

    def test_key_cert_yes_ca(self):

        """Function:  test_key_cert_yes_ca

        Description:  Test with cert and key present and with ca.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (self.svr.ssl_client_key, self.svr.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_key_cert_no_ca3(self):

        """Function:  test_key_cert_no_ca3

        Description:  Test with cert and key present, but no ca.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(self.svr.config, self.config2)

    def test_key_cert_no_ca2(self):

        """Function:  test_key_cert_no_ca2

        Description:  Test with cert and key present, but no ca.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (self.svr.ssl_client_ca, self.svr.ssl_client_flag),
            (None, mysql.connector.ClientFlag.SSL))

    def test_key_cert_no_ca(self):

        """Function:  test_key_cert_no_ca

        Description:  Test with cert and key present, but no ca.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (self.svr.ssl_client_key, self.svr.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_all2(self):

        """Function:  test_ssl_all2

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(self.svr.config, self.config3)

    def test_ssl_all(self):

        """Function:  test_ssl_all

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (self.svr.ssl_client_ca, self.svr.ssl_client_key,
             self.svr.ssl_client_cert, self.svr.ssl_client_flag),
            (self.ssl_client_ca, self.ssl_client_key, self.ssl_client_cert,
             self.ssl_client_flag))

    def test_ssl_client_cert(self):

        """Function:  test_ssl_client_cert

        Description:  Test with ssl_client_cert present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(self.svr.ssl_client_cert, self.ssl_client_cert)

    def test_ssl_client_key(self):

        """Function:  test_ssl_client_key

        Description:  Test with ssl_client_key present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_key=self.ssl_client_key)

        self.assertEqual(self.svr.ssl_client_key, self.ssl_client_key)

    def test_ssl_client_flag(self):

        """Function:  test_ssl_client_flag

        Description:  Test with ssl_client_flag present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(self.svr.ssl_client_flag, self.ssl_client_flag)

    def test_ssl_client_key_cert3(self):

        """Function:  test_ssl_client_key_cert3

        Description:  Test with both cert and key present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_key=self.ssl_client_key,
                           ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(self.svr.config, self.config2)

    def test_ssl_client_key_cert2(self):

        """Function:  test_ssl_client_key_cert2

        Description:  Test with both cert and key present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_key=self.ssl_client_key,
                           ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (self.svr.ssl_client_ca, self.svr.ssl_client_flag),
            (None, mysql.connector.ClientFlag.SSL))

    def test_ssl_client_key_cert(self):

        """Function:  test_ssl_client_key_cert

        Description:  Test with both cert and key present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_key=self.ssl_client_key,
                           ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (self.svr.ssl_client_key, self.svr.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_ca3(self):

        """Function:  test_ssl_client_flag3

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(self.svr.config, self.config)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_flag2

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(
            (self.svr.ssl_client_key, self.svr.ssl_client_cert,
             self.svr.ssl_client_flag),
            (None, None, mysql.connector.ClientFlag.SSL))

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_flag

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(self.svr.ssl_client_ca, self.ssl_client_ca)


if __name__ == "__main__":
    unittest.main()
