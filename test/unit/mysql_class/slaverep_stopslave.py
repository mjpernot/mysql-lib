#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_stopslave.py

    Description:  Unit testing of SlaveRep.stop_slave in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_stopslave.py

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
import mysql_class
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_value -> Test with values returned.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

        self.show_stat = [{"Slave_IO_State": "Down",
                           "Seconds_Behind_Master": "20"}]

    @mock.patch("mysql_class.slave_stop")
    @mock.patch("mysql_class.show_slave_stat")
    def test_value(self, mock_stat, mock_stop):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_stop.return_value = True
        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.stop_slave()
        self.assertEqual((mysqlrep.io_state, mysqlrep.secs_behind),
                         ("Down", "20"))


if __name__ == "__main__":
    unittest.main()
