# Classification (U)

"""Program:  masterrep_getloginfo.py

    Description:  Unit testing of MasterRep.get_log_info in mysql_class.py.

    Usage:
        test/unit/mysql_class/masterrep_getloginfo.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "d"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

    def test_default(self):

        """Function:  test_default

        Description:  Test get_log_info method.

        Arguments:

        """

        mysqlrep = mysql_class.MasterRep(self.name, self.server_id,
                                         self.sql_user, self.sql_pass,
                                         self.machine,
                                         defaults_file=self.defaults_file)

        self.assertEqual((mysqlrep.get_log_info()), (None, None))


if __name__ == "__main__":
    unittest.main()
