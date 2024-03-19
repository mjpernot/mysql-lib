# Classification (U)

"""Program:  slaverep_updslvstatus.py

    Description:  Unit testing of SlaveRep.upd_slv_status in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_updslvstatus.py

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
import mysql_class
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_post_8026
        test_pre_8026
        test_post_8022
        test_pre_8022
        test_run
        test_run_pre
        test_none_secsbehind
        test_int_secsbehind
        test_string_secsbehind
        test_except_secsbehind -> Test raising exception: Seconds_Behind_Master
        test_int_skipcounter
        test_string_skipcounter
        test_except_skipcounter
        test_int_masterserverid
        test_string_masterserverid
        test_except_masterserverid
        test_int_lastsqlerror
        test_string_lastsqlerror
        test_except_lastsqlerror
        test_int_lastioerror
        test_string_lastioerror
        test_except_lastioerror
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
        self.version = (5, 7, 33)
        self.version2 = (8, 0, 0)
        self.version3 = (8, 0, 21)
        self.version4 = (8, 0, 23)
        self.version5 = (8, 0, 28)
        self.fetch_vars = [
            {"Slave_running": "ON"}, {"Slave_retried_transactions": 0},
            {"Slave_open_temp_tables": "1"}]
        self.fetch_vars2 = [{"Slave_open_temp_tables": "1"}]
        self.fetch_vars3 = [{"Replica_open_temp_tables": "1"}]
        self.query = [
            [{"SERVICE_STATE": "ON"}], [{"COUNT_TRANSACTIONS_RETRIES": 0}]]
        self.read_only = {"read_only": "ON"}

        self.show_stat = [
            {"Slave_IO_State": "up",
             "Master_Host": "masterhost",
             "Master_Port": "masterport",
             "Connect_Retry": "conn_retry",
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
        self.show_stat2 = [
            {"Replica_IO_State": "up",
             "Source_Host": "masterhost",
             "Source_Port": "masterport",
             "Connect_Retry": "conn_retry",
             "Source_Log_File": "masterlog",
             "Read_Source_Log_Pos": "masterpos",
             "Relay_Log_File": "relaylog",
             "Relay_Log_Pos": "relaypos",
             "Relay_Source_Log_File": "relaymasterlog",
             "Replica_IO_Running": "running",
             "Replica_SQL_Running": "sqlcode",
             "Replicate_Do_DB": "dodb",
             "Replicate_Ignore_DB": "ignoredb",
             "Replicate_Do_Table": "dotable",
             "Replicate_Ignore_Table": "ignoretable",
             "Replicate_Wild_Do_Table": "wilddo",
             "Replicate_Wild_Ignore_Table": "wildignore",
             "Last_Errno": "lastnumber",
             "Last_Error": "lasterror",
             "Skip_Counter": "skipcnt",
             "Exec_Source_Log_Pos": "execmasterpos",
             "Relay_Log_Space": "logspave",
             "Until_Condition": "untilcond",
             "Until_Log_File": "untilog",
             "Until_Log_Pos": "untilpos",
             "Source_SSL_Allowed": "sslallow",
             "Source_SSL_CA_File": "sslcafile",
             "Source_SSL_CA_Path": "sslcapath",
             "Source_SSL_Cert": "sslcert",
             "Source_SSL_Cipher": "cipher",
             "Source_SSL_Key": "sllkey",
             "Seconds_Behind_Source": "secsbehind",
             "Source_SSL_Verify_Server_Cert": "sslverify",
             "Last_IO_Errno": "lastionumber",
             "Last_IO_Error": "lastioerror",
             "Last_SQL_Errno": "lastsqlnumber",
             "Last_SQL_Error": "lastsqlerror",
             "Replicate_Ignore_Server_Ids": "ignoreids",
             "Source_Server_Id": "serverid",
             "Source_UUID": "uuid",
             "Source_Info_File": "infofile",
             "SQL_Delay": "delay",
             "SQL_Remaining_Delay": "remaindelay",
             "Replica_SQL_Running_State": "sqlstate",
             "Source_Retry_Count": "retrycnt",
             "Source_Bind": "bind",
             "Last_IO_Error_Timestamp": "iotime",
             "Last_SQL_Error_Timestamp": "sqltime",
             "Source_SSL_Crl": "sslcrl",
             "Source_SSL_Crlpath": "sslpath",
             "Retrieved_Gtid_Set": "retgtid",
             "Executed_Gtid_Set": "exegtid",
             "Auto_Position": "autopos"}]

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.Server.col_sql")
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_post_8026(self, mock_stat, mock_global, mock_var, mock_qry):

        """Function:  test_post_8026

        Description:  Test with post-MySQL 8.0.26.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars3
        mock_stat.return_value = self.show_stat2
        mock_qry.side_effect = self.query

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version5
        mysqlrep.upd_slv_status()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.tmp_tbl), ("up", "1"))

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.Server.col_sql")
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_pre_8026(self, mock_stat, mock_global, mock_var, mock_qry):

        """Function:  test_pre_8026

        Description:  Test with pre-MySQL 8.0.26.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars2
        mock_stat.return_value = self.show_stat2
        mock_qry.side_effect = self.query

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version4
        mysqlrep.upd_slv_status()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.tmp_tbl), ("up", "1"))

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.Server.col_sql")
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_post_8022(self, mock_stat, mock_global, mock_var, mock_qry):

        """Function:  test_post_8022

        Description:  Test with post-MySQL 8.0.22, but pre-MySQL 8.0.26.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars2
        mock_stat.return_value = self.show_stat2
        mock_qry.side_effect = self.query

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version4
        mysqlrep.upd_slv_status()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.mst_host), ("up", "masterhost"))

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.Server.col_sql")
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_pre_8022(self, mock_stat, mock_global, mock_var, mock_qry):

        """Function:  test_pre_8022

        Description:  Test with pre-MySQL 8.0.22, but post-MySQL 8.0.0.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars2
        mock_stat.return_value = self.show_stat
        mock_qry.side_effect = self.query

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version3
        mysqlrep.upd_slv_status()

        self.assertEqual(
            (mysqlrep.io_state, mysqlrep.mst_host), ("up", "masterhost"))

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.Server.col_sql")
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_run(self, mock_stat, mock_global, mock_var, mock_qry):

        """Function:  test_run

        Description:  Test with run attribute in MySQL 8.0.0.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars2
        mock_stat.return_value = self.show_stat
        mock_qry.side_effect = self.query

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version2
        mysqlrep.upd_slv_status()

        self.assertEqual((mysqlrep.run, mysqlrep.tran_retry), ("ON", 0))

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_run_pre(self, mock_stat, mock_global, mock_var):

        """Function:  test_run_pre

        Description:  Test with run attribute in pre-MySQL 8.0.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual((mysqlrep.run, mysqlrep.tran_retry), ("ON", 0))

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_none_secsbehind(self, mock_stat, mock_global, mock_var):

        """Function:  test_none_secsbehind

        Description:  Test None for Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = None

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.secs_behind, "null")

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_int_secsbehind(self, mock_stat, mock_global, mock_var):

        """Function:  test_int_secsbehind

        Description:  Test integer for Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = 1

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.secs_behind, 1)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_string_secsbehind(self, mock_stat, mock_global, mock_var):

        """Function:  test_string_secsbehind

        Description:  Test string for Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = "1"

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.secs_behind, 1)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_except_secsbehind(self, mock_stat, mock_global, mock_var):

        """Function:  test_except_secsbehind

        Description:  Test raising exception for Seconds_Behind_Master.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.secs_behind, "null")

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_int_skipcounter(self, mock_stat, mock_global, mock_var):

        """Function:  test_int_skipcounter

        Description:  Test integer for Skip_Counter.

        Arguments:

        """

        self.show_stat[0]["Skip_Counter"] = 1

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.skip_ctr, 1)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_string_skipcounter(self, mock_stat, mock_global, mock_var):

        """Function:  test_string_skipcounter

        Description:  Test string for Skip_Counter.

        Arguments:

        """

        self.show_stat[0]["Skip_Counter"] = "1"

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.skip_ctr, 1)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_except_skipcounter(self, mock_stat, mock_global, mock_var):

        """Function:  test_except_skipcounter

        Description:  Test raising exception for Skip_Counter.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.skip_ctr, "skipcnt")

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_int_masterserverid(self, mock_stat, mock_global, mock_var):

        """Function:  test_int_masterserverid

        Description:  Test integer for Master_Server_Id.

        Arguments:

        """

        self.show_stat[0]["Master_Server_Id"] = 11

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.mst_id, 11)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_string_masterserverid(self, mock_stat, mock_global, mock_var):

        """Function:  test_string_masterserverid

        Description:  Test string for Master_Server_Id.

        Arguments:

        """

        self.show_stat[0]["Master_Server_Id"] = "11"

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.mst_id, 11)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_except_masterserverid(self, mock_stat, mock_global, mock_var):

        """Function:  test_except_masterserverid

        Description:  Test raising exception for Master_Server_Id.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.mst_id, "serverid")

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_int_lastsqlerror(self, mock_stat, mock_global, mock_var):

        """Function:  test_int_lastsqlerror

        Description:  Test integer for Last_SQL_Errno.

        Arguments:

        """

        self.show_stat[0]["Last_SQL_Errno"] = 1

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.sql_err, 1)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_string_lastsqlerror(self, mock_stat, mock_global, mock_var):

        """Function:  test_string_lastsqlerror

        Description:  Test string for Last_SQL_Errno.

        Arguments:

        """

        self.show_stat[0]["Last_SQL_Errno"] = "1"

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.sql_err, 1)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_except_lastsqlerror(self, mock_stat, mock_global, mock_var):

        """Function:  test_except_lastsqlerror

        Description:  Test raising exception for Last_SQL_Errno.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.sql_err, "lastsqlnumber")

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_int_lastioerror(self, mock_stat, mock_global, mock_var):

        """Function:  test_int_lastioerror

        Description:  Test integer for Last_IO_Errno.

        Arguments:

        """

        self.show_stat[0]["Last_IO_Errno"] = 1

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.io_err, 1)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_string_lastioerror(self, mock_stat, mock_global, mock_var):

        """Function:  test_string_lastioerror

        Description:  Test string for Last_IO_Errno.

        Arguments:

        """

        self.show_stat[0]["Last_IO_Errno"] = "1"

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.io_err, 1)

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_except_lastioerror(self, mock_stat, mock_global, mock_var):

        """Function:  test_except_lastioerror

        Description:  Test raising exception for Last_IO_Errno.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual(mysqlrep.io_err, "lastionumber")

    @mock.patch(
        "mysql_class.SlaveRep.upd_gtid_pos", mock.Mock(return_value=True))
    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_value(self, mock_stat, mock_global, mock_var):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_var.return_value = self.read_only
        mock_global.side_effect = self.fetch_vars
        mock_stat.return_value = self.show_stat

        mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            self.machine, defaults_file=self.defaults_file)
        mysqlrep.version = self.version
        mysqlrep.upd_slv_status()

        self.assertEqual((mysqlrep.io_state, mysqlrep.slv_io,
                          mysqlrep.slv_sql, mysqlrep.auto_pos),
                         ("up", "running", "sqlcode", "autopos"))


if __name__ == "__main__":
    unittest.main()
