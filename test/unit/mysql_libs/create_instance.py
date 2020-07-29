#!/usr/bin/python
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

    def __init__(self, name, sid, user, pswd, machine, host, port,
                 defaults_file, extra_def_file=None):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.sid = sid
        self.user = user
        self.pswd = pswd
        self.serv_os = machine
        self.host = host
        self.port = port
        self.cfg_file = defaults_file
        self.extra_def_file = extra_def_file


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
        self.extra_def_file = "extra_def_file"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_create_instance -> Test create_instance function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Cfg = Cfg()
        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.passwd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"
        self.server = Server(
            self.name, self.sid, self.user, self.passwd, self.serv_os,
            self.host, self.port, self.cfg_file)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_create_instance(self, mock_cfg):

        """Function:  test_create_instance

        Description:  Test create_instance function.

        Arguments:

        """

        mock_cfg.return_value = self.Cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(type(self.server) == type(srv_inst))


if __name__ == "__main__":
    unittest.main()
