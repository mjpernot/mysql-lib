# Classification (U)

"""Program:  masterrep_updmststatus.py

    Description:  Unit testing of MasterRep.upd_mst_status in mysql_class.py.

    Usage:
        test/unit/mysql_class/masterrep_updmststatus.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

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
        test_slaves
        test_value

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

        self.show_stat = [{"Executed_Gtid_Set": "23678"}]
        self.show_slaves = [
            {"Server_ID": 20, "Host": "Hostname", "Port": 3306,
             "Source_ID": 10, "Replica_UUID": "Unique_Number"}]

    @mock.patch("mysql_class.MasterRep.show_slv_hosts")
    @mock.patch("mysql_class.Server.upd_log_stats")
    @mock.patch("mysql_class.show_master_stat")
    def test_slaves(self, mock_stat, mock_log, mock_slvs):

        """Function:  test_slaves

        Description:  Test with values returned.

        Arguments:

        """

        mock_log.return_value = True
        mock_stat.return_value = self.show_stat
        mock_slvs.return_value = self.show_slaves
        mysqldb = mysql_class.MasterRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        mysqldb.upd_mst_status()
        self.assertEqual((mysqldb.slaves), self.show_slaves)

    @mock.patch("mysql_class.MasterRep.show_slv_hosts")
    @mock.patch("mysql_class.Server.upd_log_stats")
    @mock.patch("mysql_class.show_master_stat")
    def test_value(self, mock_stat, mock_log, mock_slvs):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_log.return_value = True
        mock_stat.return_value = self.show_stat
        mock_slvs.return_value = self.show_slaves
        mysqldb = mysql_class.MasterRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)

        mysqldb.upd_mst_status()
        self.assertEqual((mysqldb.exe_gtid), ("23678"))


if __name__ == "__main__":
    unittest.main()
