#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_startslave.py

    Description:  Unit testing of SlaveRep.start_slave in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_startslave.py

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

        self.show_stat = [{"Slave_IO_State": "Up",
                           "Seconds_Behind_Master": "20"}]

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_int_secsbehindmaster(self, mock_stat):

        """Function:  test_int_secsbehindmaster

        Description:  Test integer for Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = 20

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.start_slave()
        self.assertEqual((mysqlrep.io_state, mysqlrep.secs_behind),
                         ("Up", 20))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_string_secsbehindmaster(self, mock_stat):

        """Function:  test_string_secsbehindmaster

        Description:  Test string for Seconds_Behind_Master.

        Arguments:

        """

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.start_slave()
        self.assertEqual((mysqlrep.io_state, mysqlrep.secs_behind),
                         ("Up", 20))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_except_secsbehindmaster(self, mock_stat):

        """Function:  test_except_secsbehindmaster

        Description:  Test raising exception: Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = "time"

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.start_slave()
        self.assertEqual((mysqlrep.io_state, mysqlrep.secs_behind),
                         ("Up", "time"))

    @mock.patch("mysql_class.slave_start", mock.Mock(return_value=True))
    @mock.patch("mysql_class.show_slave_stat")
    def test_value(self, mock_stat):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.start_slave()
        self.assertEqual((mysqlrep.io_state, mysqlrep.secs_behind),
                         ("Up", 20))


if __name__ == "__main__":
    unittest.main()
