# Classification (U)

"""Program:  create_instance.py

    Description:  Unit testing of create_instance in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/create_instance.py

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
import mysql.connector
import mock

# Local
sys.path.append(os.getcwd())
import mysql_libs
import version

__version__ = version.__version__


class SlaveRep(object):

    """Class:  SlaveRep

    Description:  Class stub holder for SlaveRep class.

    Methods:
        __init__

    """

    def __init__(self, name, sid, user, japd, **kwargs):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.sid = sid
        self.user = user
        self.japd = japd
        self.serv_os = kwargs.get("machine")
        self.host = kwargs.get("host")
        self.port = kwargs.get("port")
        self.cfg_file = kwargs.get("defaults_file")
        self.extra_def_file = kwargs.get("extra_def_file", None)
        self.rep_user = kwargs.get("rep_user", None)
        self.rep_japd = kwargs.get("rep_japd", None)


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__

    """

    def __init__(self, name, sid, user, japd, **kwargs):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.sid = sid
        self.user = user
        self.japd = japd
        self.serv_os = kwargs.get("machine")
        self.host = kwargs.get("host")
        self.port = kwargs.get("port")
        self.cfg_file = kwargs.get("defaults_file")
        self.extra_def_file = kwargs.get("extra_def_file", None)
        self.ssl_client_ca = kwargs.get("ssl_client_ca", None)
        self.ssl_client_key = kwargs.get("ssl_client_key", None)
        self.ssl_client_cert = kwargs.get("ssl_client_cert", None)
        self.ssl_client_flag = kwargs.get("ssl_client_flag",
                                          mysql.connector.ClientFlag.SSL)
        self.ssl_disabled = kwargs.get("ssl_disabled", False)
        self.ssl_verify_id = kwargs.get("ssl_verify_id", False)
        self.ssl_verify_cert = kwargs.get("ssl_verify_cert", False)


class Cfg(object):

    """Class:  Cfg

    Description:  Stub holder for configuration file.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.japd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"


class Cfg2(object):

    """Class:  Cfg2

    Description:  Stub holder for configuration file.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.japd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"
        self.rep_user = "rep_user"
        self.rep_japd = "rep_japd"


class Cfg3(object):

    """Class:  Cfg3

    Description:  Stub holder for configuration file.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.japd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"
        self.ssl_client_ca = None
        self.ssl_client_key = None
        self.ssl_client_cert = None
        self.ssl_client_flag = None
        self.ssl_disabled = False
        self.ssl_verify_id = False
        self.ssl_verify_cert = False


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_set_ssl_verify_cert
        test_set_ssl_verify_id
        test_set_ssl_disabled
        test_set_ssl_flag
        test_set_ssl_cert
        test_set_ssl_key
        test_set_ssl_ca2
        test_set_ssl_ca
        test_none_ssl_verify_cert
        test_none_ssl_verify_id
        test_none_ssl_disabled
        test_none_ssl_flag
        test_none_ssl_cert
        test_none_ssl_key
        test_none_ssl_ca2
        test_none_ssl_ca
        test_no_ssl_verify_cert
        test_no_ssl_verify_id
        test_no_ssl_disabled
        test_no_ssl_flag
        test_no_ssl_cert
        test_no_ssl_key
        test_no_ssl_ca2
        test_no_ssl_ca
        test_rep_user2
        test_rep_user
        test_none_rep_user2
        test_none_rep_user
        test_none_extra_def_file2
        test_none_extra_def_file
        test_create_instance

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = Cfg()
        self.cfg2 = Cfg2()
        self.cfg3 = Cfg3()
        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.japd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"
        self.server = Server(
            self.name, self.sid, self.user, self.japd, machine=self.serv_os,
            host=self.host, port=self.port, defaults_file=self.cfg_file)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_set_ssl_verify_cert(self, mock_cfg):

        """Function:  test_set_ssl_verify_cert

        Description:  Test with SSL Verify Cert set to True.

        Arguments:

        """

        self.cfg3.ssl_verify_cert = True

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(srv_inst.ssl_verify_cert)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_set_ssl_verify_id(self, mock_cfg):

        """Function:  test_set_ssl_verify_id

        Description:  Test with SSL Verify ID set to True.

        Arguments:

        """

        self.cfg3.ssl_verify_id = True

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(srv_inst.ssl_verify_id)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_set_ssl_disabled(self, mock_cfg):

        """Function:  test_set_ssl_disabled

        Description:  Test with SSL Disabled set to True.

        Arguments:

        """

        self.cfg3.ssl_disabled = True

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(srv_inst.ssl_disabled)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_set_ssl_flag(self, mock_cfg):

        """Function:  test_set_ssl_flag

        Description:  Test with SSL Client Flag set.

        Arguments:

        """

        self.cfg3.ssl_client_flag = 4096

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.ssl_client_flag, self.cfg3.ssl_client_flag)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_set_ssl_cert(self, mock_cfg):

        """Function:  test_set_ssl_cert

        Description:  Test with SSL Client Cert set.

        Arguments:

        """

        self.cfg3.ssl_client_key = "SSL_Client_Cert"

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.ssl_client_cert, self.cfg3.ssl_client_cert)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_set_ssl_key(self, mock_cfg):

        """Function:  test_set_ssl_key

        Description:  Test with SSL Client Key set.

        Arguments:

        """

        self.cfg3.ssl_client_key = "SSL_Client_Key"

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.ssl_client_key, self.cfg3.ssl_client_key)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_set_ssl_ca2(self, mock_cfg):

        """Function:  test_set_ssl_ca2

        Description:  Test with SSL Client CA set.

        Arguments:

        """

        self.cfg3.ssl_client_ca = "SSL_Client_CA"

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.ssl_client_ca, self.cfg3.ssl_client_ca)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_set_ssl_ca(self, mock_cfg):

        """Function:  test_set_ssl_ca

        Description:  Test with SSL Client CA set.

        Arguments:

        """

        self.cfg3.ssl_client_ca = "SSL_Client_CA"

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_ssl_verify_cert(self, mock_cfg):

        """Function:  test_none_ssl_verify_cert

        Description:  Test with SSL Verify Cert set to None.

        Arguments:

        """

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_verify_cert)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_ssl_verify_id(self, mock_cfg):

        """Function:  test_none_ssl_verify_id

        Description:  Test with SSL Verify ID set to None.

        Arguments:

        """

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_verify_id)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_ssl_disabled(self, mock_cfg):

        """Function:  test_none_ssl_disabled

        Description:  Test with SSL Disabled set to None.

        Arguments:

        """

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_disabled)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_ssl_flag(self, mock_cfg):

        """Function:  test_none_ssl_flag

        Description:  Test with SSL Client Flag set to None.

        Arguments:

        """

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.ssl_client_flag,
                         mysql.connector.ClientFlag.SSL)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_ssl_cert(self, mock_cfg):

        """Function:  test_none_ssl_cert

        Description:  Test with SSL Client Cert set to None.

        Arguments:

        """

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_client_cert)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_ssl_key(self, mock_cfg):

        """Function:  test_none_ssl_key

        Description:  Test with SSL Client Key set to None.

        Arguments:

        """

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_client_key)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_ssl_ca2(self, mock_cfg):

        """Function:  test_none_ssl_ca2

        Description:  Test with SSL Client CA set to None.

        Arguments:

        """

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_client_ca)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_ssl_ca(self, mock_cfg):

        """Function:  test_none_ssl_ca

        Description:  Test with SSL Client CA set to None.

        Arguments:

        """

        mock_cfg.return_value = self.cfg3

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_no_ssl_verify_cert(self, mock_cfg):

        """Function:  test_no_ssl_verify_cert

        Description:  Test with no SSL Verify Cert passed.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_verify_cert)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_no_ssl_verify_id(self, mock_cfg):

        """Function:  test_no_ssl_verify_id

        Description:  Test with no SSL Verify ID passed.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_verify_id)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_no_ssl_disabled(self, mock_cfg):

        """Function:  test_no_ssl_disabled

        Description:  Test with no SSL Disabled passed.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_disabled)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_no_ssl_flag(self, mock_cfg):

        """Function:  test_no_ssl_flag

        Description:  Test with no SSL Client Flag passed.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.ssl_client_flag,
                         mysql.connector.ClientFlag.SSL)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_no_ssl_cert(self, mock_cfg):

        """Function:  test_no_ssl_cert

        Description:  Test with no SSL Client Cert passed.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_client_cert)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_no_ssl_key(self, mock_cfg):

        """Function:  test_no_ssl_key

        Description:  Test with no SSL Client Key passed.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_client_key)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_no_ssl_ca2(self, mock_cfg):

        """Function:  test_no_ssl_ca2

        Description:  Test with no SSL Client CA passed.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertFalse(srv_inst.ssl_client_ca)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_no_ssl_ca(self, mock_cfg):

        """Function:  test_no_ssl_ca

        Description:  Test with no SSL Client CA passed.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_rep_user2(self, mock_cfg):

        """Function:  test_rep_user2

        Description:  Test with for rep_user.

        Arguments:

        """

        mock_cfg.return_value = self.cfg2

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", SlaveRep)

        self.assertEqual(srv_inst.__dict__.get("rep_user", None),
                         self.cfg2.rep_user)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_rep_user(self, mock_cfg):

        """Function:  test_rep_user

        Description:  Test with for rep_user.

        Arguments:

        """

        mock_cfg.return_value = self.cfg2

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", SlaveRep)

        self.assertTrue(isinstance(srv_inst, SlaveRep))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_rep_user2(self, mock_cfg):

        """Function:  test_none_rep_user2

        Description:  Test with none for rep_user.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.__dict__.get("rep_user", None), None)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_rep_user(self, mock_cfg):

        """Function:  test_none_rep_user

        Description:  Test with none for rep_user.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_extra_def_file2(self, mock_cfg):

        """Function:  test_none_extra_def_file2

        Description:  Test with none for extra_def_file.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        self.cfg.extra_def_file = None

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.extra_def_file, None)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_extra_def_file(self, mock_cfg):

        """Function:  test_none_extra_def_file

        Description:  Test with none for extra_def_file.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        self.cfg.extra_def_file = None

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_create_instance(self, mock_cfg):

        """Function:  test_create_instance

        Description:  Test create_instance function.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))


if __name__ == "__main__":
    unittest.main()
