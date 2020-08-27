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
        self.japd = None
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
        test_none_extra_def_file -> Test with none for extra_def_file.
        test_create_instance -> Test create_instance function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = Cfg()
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
    def test_none_extra_def_file(self, mock_cfg):

        """Function:  test_none_extra_def_file

        Description:  Test with none for extra_def_file.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        self.cfg.extra_def_file = None

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))
        self.assertEqual(srv_inst.extra_def_file, None)

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
