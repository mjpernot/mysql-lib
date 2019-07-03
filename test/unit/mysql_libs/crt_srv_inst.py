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

# Local
sys.path.append(os.getcwd())
import mysql_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, name, sid, user, pwd, serv_os, host, port, cfg_file):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        self.name = name
        self.sid = sid
        self.user = user
        self.pwd = pwd
        self.serv_os = serv_os
        self.host = host
        self.port = port
        self.cfg_file = cfg_file


class Cfg(object):

    """Class:  Cfg

    Description:  Stub holder for configuration file.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.pwd = "pwd"
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_crt_srv_inst -> Test crt_srv_inst function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Server = Server()
        self.Cfg = Cfg()

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_crt_srv_inst(self, mock_cfg):

        """Function:  test_crt_srv_inst

        Description:  Test crt_srv_inst function.

        Arguments:

        """

        mock_cfg.return_value = self.Cfg

        self.assertEqual(mysql_libs.crt_srv_inst("Cfgfile", "DirPath"),
                         self.Server)


if __name__ == "__main__":
    unittest.main()
