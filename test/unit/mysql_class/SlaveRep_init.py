#!/usr/bin/python
# Classification (U)

"""Program:  SlaveRep_init.py

    Description:  Unit testing of SlaveRep.__init__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/SlaveRep_init.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_pwd"
        self.machine = "Linux"
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

        self.show_stat = [{"Slave_IO_State": "up",
                          "Master_Host": "masterhost",
                          "Master_Port": "masterport",
                          "Connect_Retry": "retry",
                          "Master_Log_File": "masterlog",
                          "Read_Master_Log_Pos": "masterpos",
                          "Relay_Log_File": "relaylog",
                          "Relay_Log_Pos": "relaypos",
                          "Relay_Master_Log_File": "relaymasterlog",
                          "Slave_IO_Running": "running",
                          "Slave_SQL_Running": "sqlcode",
                          "Replicate_Do_DB": "dodb",
                          "Replicate_Ignore_DB": "ignoredb",
                          "Replicate_Do_Table": "dotable",
                          "Replicate_Ignore_Table": "ignoretable",
                          "Replicate_Wild_Do_Table": "wilddo",
                          "Replicate_Wild_Ignore_Table": "wildignore",
                          "Last_Errno": "lastnumber",
                          "Last_Error": "lasterror",
                          "Skip_Counter": "skipcnt",
                          "Exec_Master_Log_Pos": "execmasterpos",
                          "Relay_Log_Space": "logspave",
                          "Until_Condition": "untilcond",
                          "Until_Log_File": "untilog",
                          "Until_Log_Pos": "untilpos",
                          "Master_SSL_Allowed": "sslallow",
                          "Master_SSL_CA_File": "sslcafile",
                          "Master_SSL_CA_Path": "sslcapath",
                          "Master_SSL_Cert": "sslcert",
                          "Master_SSL_Cipher": "cipher",
                          "Master_SSL_Key": "sllkey",
                          "Seconds_Behind_Master": "secsbehind",
                          "Master_SSL_Verify_Server_Cert": "sslverify",
                          "Last_IO_Errno": "lastionumber",
                          "Last_IO_Error": "lastioerror",
                          "Last_SQL_Errno": "lastsqlnumber",
                          "Last_SQL_Error": "lastsqlerror",
                          "Replicate_Ignore_Server_Ids": "ignoreids",
                          "Master_Server_Id": "serverid",
                          "Master_UUID": "uuid",
                          "Master_Info_File": "infofile",
                          "SQL_Delay": "delay",
                          "SQL_Remaining_Delay": "remaindelay",
                          "Slave_SQL_Running_State": "sqlstate",
                          "Master_Retry_Count": "retrycnt",
                          "Master_Bind": "bind",
                          "Last_IO_Error_Timestamp": "iotime",
                          "Last_SQL_Error_Timestamp": "sqltime",
                          "Master_SSL_Crl": "sslcrl",
                          "Master_SSL_Crlpath": "sslpath",
                          "Retrieved_Gtid_Set": "retgtid",
                          "Executed_Gtid_Set": "exegtid",
                          "Auto_Position": "autopos"}]

    @mock.patch("mysql_class.SlaveRep.upd_gtid_pos")
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_default(self, mock_stat, mock_global, mock_var, mock_gtid):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mock_gtid.return_value = True
        mock_var.return_value = {"read_only": "ON"}
        mock_global.side_effect = [{"slave_running": "Value"},
                                   {"slave_open_temp_tables": "Value"},
                                   {"slave_retried_transactions": "Value"}]
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        self.assertEqual((mysqlrep.name, mysqlrep.server_id,
                          mysqlrep.sql_user, mysqlrep.sql_pass,
                          mysqlrep.machine, mysqlrep.host, mysqlrep.port,
                          mysqlrep.run),
                         (self.name, self.server_id, self.sql_user,
                          self.sql_pass, self.machine, "localhost", 3306,
                          "Value"))


if __name__ == "__main__":
    unittest.main()
