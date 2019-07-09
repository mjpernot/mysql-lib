#!/usr/bin/python
# Classification (U)

"""Program:  crt_cmd.py

    Description:  Unit testing of crt_cmd in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/crt_cmd.py

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

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        self.name = "name"
        self.sid = "sid"
        self.sql_user = "user"
        self.sql_pass = "pwd"
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_no_extra_def_file -> Test with no extra_def_file present.
        test_extra_def_file -> Test with extra_def_file present.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.Server = Server()
        self.prog1 = ["Program",
                      "--defaults-extra-file=" + self.Server.extra_def_file,
                      "-u", self.Server.sql_user,
                      "-h", self.Server.host, "-P",
                      str(self.Server.port)]
        self.prog2 = ["Program", "-u", self.Server.sql_user,
                      "-p" + self.Server.sql_pass, "-h", self.Server.host,
                      "-P", str(self.Server.port)]

    def test_no_extra_def_file(self):

        """Function:  test_no_extra_def_file

        Description:  Test with no extra_def_file present.

        Arguments:

        """

        self.Server.extra_def_file = None

        self.assertEqual(mysql_libs.crt_cmd(self.Server, "Program"),
                         self.prog2)

    def test_extra_def_file(self):

        """Function:  test_extra_def_file

        Description:  Test with extra_def_file present.

        Arguments:

        """

        self.assertEqual(mysql_libs.crt_cmd(self.Server, "Program"),
                         self.prog1)


if __name__ == "__main__":
    unittest.main()
