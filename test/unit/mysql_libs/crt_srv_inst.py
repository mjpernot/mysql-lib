#!/usr/bin/python
# Classification (U)

"""Program:  crt_srv_inst.py

    Description:  Unit testing of crt_srv_inst in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/crt_srv_inst.py

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
import mysql_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, name, sid, user, pswd, serv_os, host, port, cfg_file):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.sid = sid
        self.user = user
        self.pswd = pswd
        self.serv_os = serv_os
        self.host = host
        self.port = port
        self.cfg_file = cfg_file


class Cfg(object):

    """Class:  Cfg

    Description:  Stub holder for configuration file.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.passwd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_crt_srv_inst -> Test crt_srv_inst function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Cfg = Cfg()
        self.Server = Server(self.Cfg.name, self.Cfg.sid, self.Cfg.user,
                             self.Cfg.passwd, self.Cfg.serv_os, self.Cfg.host,
                             self.Cfg.port, self.Cfg.cfg_file)

    @mock.patch("mysql_libs.mysql_class.Server")
    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_crt_srv_inst(self, mock_cfg, mock_srv):

        """Function:  test_crt_srv_inst

        Description:  Test crt_srv_inst function.

        Arguments:

        """

        mock_cfg.return_value = self.Cfg
        mock_srv.return_value = self.Server

        instance = mysql_libs.crt_srv_inst("Cfgfile", "DirPath")
        self.assertEqual(type(instance), type(self.Server))


if __name__ == "__main__":
    unittest.main()
