#!/usr/bin/python
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

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mysql_class
import lib.gen_libs as gen_libs
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_ssl_all -> Test with all ssl arguments present.
        test_ssl_client_cert -> Test with ssl_client_cert only.
        test_ssl_client_key -> Test with ssl_client_key only.
        test_ssl_client_flags -> Test with ssl_client_flags present.
        test_ssl_client_key_cert2 -> Test with both cert and key present.
        test_ssl_client_key_cert -> Test with both cert and key present.
        test_ssl_client_sa2 -> Test with ssl_client_sa only present.
        test_ssl_client_sa -> Test with ssl_client_sa only present.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mysql_cfg"
        cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)

        self.ssl_client_sa = "sa_file"
        self.ssl_client_key = "key_file"
        self.ssl_client_cert = "cert_file"
        self.ssl_client_flags = [2048]

# Another to test self.config

    def test_ssl_all(self):

        """Function:  test_ssl_all

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        self.svr.setup_ssl(
            ssl_client_sa=self.ssl_client_sa,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flags=self.ssl_client_flags)

        self.assertEqual(
            (self.svr.ssl_client_sa, self.svr.ssl_client_key,
             self.svr.ssl_client_cert, self.svr.ssl_client_flags),
            (self.ssl_client_sa, self.ssl_client_key, self.ssl_client_cert,
             self.ssl_client_flags))

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

    def test_ssl_client_flags(self):

        """Function:  test_ssl_client_flags

        Description:  Test with ssl_client_flags present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_flags=self.ssl_client_flags)

        self.assertEqual(self.svr.ssl_client_flags, self.ssl_client_flags)

# Another to test self.config

    def test_ssl_client_key_cert2(self):

        """Function:  test_ssl_client_key_cert2

        Description:  Test with both cert and key present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_key=self.ssl_client_key,
                           ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (self.svr.ssl_client_sa, self.svr.ssl_client_flags), (None, []))

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

# Another to test self.config

    def test_ssl_client_sa2(self):

        """Function:  test_ssl_client_flags2

        Description:  Test with ssl_client_sa only present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_sa=self.ssl_client_sa)

        self.assertEqual(
            (self.svr.ssl_client_key, self.svr.ssl_client_cert,
             self.svr.ssl_client_flags), (None, None, []))

    def test_ssl_client_sa(self):

        """Function:  test_ssl_client_flags

        Description:  Test with ssl_client_sa only present.

        Arguments:

        """

        self.svr.setup_ssl(ssl_client_sa=self.ssl_client_sa)

        self.assertEqual(self.svr.ssl_client_sa, self.ssl_client_sa)


if __name__ == "__main__":
    unittest.main()
