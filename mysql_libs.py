# Classification (U)

"""Program:  mysql_libs.py

    Description:  Library of function calls for SQL commands for a MySQL
        database.

    Functions:
        analyze_tbl
        change_master_to
        checksum
        check_tbl
        chg_slv_state
        create_instance
        create_slv_array
        crt_cmd
        crt_srv_inst
        fetch_db_dict
        fetch_logs
        fetch_slv
        fetch_tbl_dict
        find_name
        is_cfg_valid
        is_logs_synced
        is_rep_delay
        optimize_tbl
        purge_bin_logs
        reset_master
        reset_slave
        select_wait_until
        start_slave_until
        switch_to_master
        sync_delay
        sync_rep_slv
        wait_until
        _io_chk
        _sql_chk

"""

# Libraries and Global Variables

# Standard
import time

# Local
import lib.gen_libs as gen_libs
import lib.machine as machine
import mysql_class
import version

__version__ = version.__version__


def analyze_tbl(SERVER, db, tbl, res_set="all", **kwargs):

    """Function:  analyze_tbl

    Description:  Runs a analyze table command against a table.

    Arguments:
        (input) SERVER -> Server instance.
        (input) db -> Database name.
        (input) tbl -> Table name.
        (input) res_set -> row|all - Returning result set format.
        (output) Return check table results.

    """

    # Must have back ticks around names if they have special characters.
    sql_cmd = "analyze table `" + db + "`.`" + tbl + "`"

    return SERVER.sql(sql_cmd, res_set)


def change_master_to(MST, SLV):

    """Function:  change_master_to

    Description:  Changes a slave to point to a master using either the
        master's binary log file and position for non-GTID databases or using
        the auto position option if GTID is enabled.

    Arguments:
        (input) MST -> Master class instance.
        (input) SLV -> Slave class instance.

    """

    chg_master_to = """change master to master_host=%s, master_port=%s,
        master_user=%s, master_password=%s"""

    # GTID mode is enabled, use the auto position option.
    if MST.gtid_mode:
        chg_master_to = chg_master_to + """, master_auto_position=1"""

        SLV.sql(chg_master_to, "", (MST.host, int(MST.port), MST.sql_user,
                                    MST.sql_pass))

    # Assume GTID mode is disabled, use file and position options.
    else:
        chg_master_to = chg_master_to + \
            """, master_log_file=%s, master_log_pos=%s"""

        SLV.sql(chg_master_to, "", (MST.host, int(MST.port), MST.sql_user,
                                    MST.sql_pass, MST.file, MST.pos))

    print("Changed Slave: {0} to new Master: {1}".format(SLV.name, MST.name))


def checksum(SERVER, db, tbl, res_set="all"):

    """Function:  checksum

    Description:  Runs a checksum against a table.

    Arguments:
        (input) SERVER -> Server instance.
        (input) db -> Database name.
        (input) tbl -> Table name.
        (input) res_set -> row or all - Returning result set.
            Default value: 'all' will cover most requirements.
        (output) Return check sum value.

    """

    # Must have back ticks around names if they have special characters.
    sql_cmd = "checksum table `" + db + "`.`" + tbl + "`"

    return SERVER.sql(sql_cmd, res_set)


def check_tbl(SERVER, db, tbl, res_set="all", **kwargs):

    """Function:  check_tbl

    Description:  Runs a check table command against a table.

    Arguments:
        (input) SERVER -> Server instance.
        (input) db -> Database name.
        (input) tbl -> Table name.
        (input) res_set -> row|all - Returning result set format.
        (output) Return check table results.

    """

    # Must have back ticks around names if they have special characters.
    sql_cmd = "check table `" + db + "`.`" + tbl + "`"

    return SERVER.sql(sql_cmd, res_set)


def chg_slv_state(SLAVE, opt):

    """Function:  chg_slv_state

    Description:  Starts or stops all of the slaves in array of slave class
        instances.

    Arguments:
        (input) SLAVE -> Array of slave instances.
        (input) opt -> stop or start - Stops or starts the slaves.

    """

    if opt == "stop":
        for x in SLAVE:

            x.stop_slave()
            x.upd_slv_status()

    elif opt == "start":
        for x in SLAVE:

            x.start_slave()
            x.upd_slv_status()

    else:
        gen_libs.prt_msg("Error", "No option selected to stop/start rep.")


def create_instance(cfg_file, dir_path, CLASS):

    """Function:  create_instance

    Description:  Create a instance for the class received on the argument
        line.

    Arguments:
        (input) cfg_file -> Configuration file name.
        (input) dir_path -> Directory path.
        (input) CLASS -> Reference to a Class type.

    """

    cfg = gen_libs.load_module(cfg_file, dir_path)

    return CLASS(cfg.name, cfg.sid, cfg.user, cfg.passwd,
                 getattr(machine, cfg.serv_os)(), cfg.host, cfg.port,
                 cfg.cfg_file,
                 extra_def_file=cfg.__dict__.get("extra_def_file", None))


def create_slv_array(cfg_array):

    """Function:  create_slv_array

    Description:  Creates an array of instances from a configuration array.

    Arguments:
        (input) cfg_array -> Array of configurations.
        (output) SLAVE -> Array of slave instances.

    """

    SLAVE = []

    for slv in cfg_array:

        SLV_INST = mysql_class.SlaveRep(slv["name"], slv["sid"], slv["user"],
                                        slv["passwd"],
                                        getattr(machine, slv["serv_os"])(),
                                        slv["host"], int(slv["port"]),
                                        slv["cfg_file"])

        SLAVE.append(SLV_INST)

    return SLAVE


def crt_cmd(SERVER, prog_name):

    """Function:  crt_cmd

    Description:  Create a basic MySQL program command line setup.  The basic
        setup will include program name, user, passwd, host, and port.
        The port is required to be set if Mysql instance is operating
        on a different port than 3306.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) prog_name -> Name of Mysql binary program.
        (output) -> List array containing the program command.

    """

    if SERVER.extra_def_file:
        # Include defaults extra file option in command, but no password.
        return [prog_name, "--defaults-extra-file=" + SERVER.extra_def_file,
                "-u", SERVER.sql_user, "-h", SERVER.host, "-P",
                str(SERVER.port)]
    else:
        # Command with password.
        return [prog_name, "-u", SERVER.sql_user, "-p" + SERVER.sql_pass, "-h",
                SERVER.host, "-P", str(SERVER.port)]


def crt_srv_inst(cfg, path):

    """Function:  crt_srv_inst

    Description:  Create a server class instance from the configuration file.

    Arguments:
        (input) cfg -> Configuration file.
        (input) path -> Directory path to the configuration file.
        (output) -> Instance of the Server class.

    """

    db = gen_libs.load_module(cfg, path)

    return mysql_class.Server(db.name, db.sid, db.user, db.passwd,
                              getattr(machine, db.serv_os)(), db.host, db.port,
                              db.cfg_file)


def fetch_db_dict(SERVER, res_set="all"):

    """Function:  fetch_db_dict

    Description:  Return an dictionary array of all databases.

    Arguments:
        (input) SERVER -> Database server instance.
        (input) res_set -> row or all - Returning result set.
            Default value: 'all' will cover most requirements.
        (output) -> Dictionary array of database names.

    """

    return SERVER.sql("show databases", res_set)


def fetch_logs(SERVER, res_set="all"):

    """Function:  fetch_logs

    Description:  Return the output of the show binary logs command.

    Arguments:
        (input) SERVER -> Server instance.
        (input) res_set -> row or all - Returning result set.
            Default value: 'all' will cover most requirements.
        (output) Return names of the binary logs.

    """

    return SERVER.sql("show binary logs", res_set)


def fetch_slv(SLAVES, **kwargs):

    """Function:  fetch_slv

    Description:  Returns name of slave in slave array, if found.  Also returns
        error code and message if not found.

    Arguments:
        (input) SLAVE -> Slave instance array.
        (input) **kwargs:
            slv_mv -> Name of slave to be moved to new master.
        (output) SLV -> Class instance of slave.
        (output) err_flag -> True|False - if an error has occurred.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None
    SLV = None

    # Locate slave in slave array.
    SLV = find_name(SLAVES, kwargs.get("slv_mv"))

    if not SLV:
        err_flag = True
        err_msg = "Error:  Slave %s was not found in slave array." % (slv)

    return SLV, err_flag, err_msg


def fetch_tbl_dict(SERVER, db, tbl_type="BASE TABLE", res_set="all"):

    """Function:  fetch_tbl_dict

    Description:  Return a list of all tables within a database that have a
        table type of BASE TABLE.

    Arguments:
        (input) SERVER -> Server class instance.
        (input) db -> Name of database.
        (input) tbl_type -> Type of table in the database.
        (input) res_set -> row or all - Returning result set.
            Default value: 'all' will cover most requirements.
        (output) List of tables in database.

    """

    sql_qry = """select table_name from information_schema.tables where
        table_type = %s and table_schema = %s"""

    return SERVER.sql(sql_qry, res_set, (tbl_type, db))


def find_name(SLV, server_name):

    """Function:  find_name

    Description:  Locates and returns a slave's instance from an array of slave
        instances.

    Arguments:
        (input) SLV -> Slave class instance(s).
        (input) server_name -> Name of server being searched for.
        (output) Return the server's instance or None.

    """

    for x in SLV:
        if server_name == x.name:
            return x

    return None


def is_cfg_valid(SERVERS, **kwargs):

    """Function:  is_cfg_valid

    Description:  Validates the configuration file for each of the class
        server instances.

    Arguments:
        (input) SERVERS -> List of class server instances.
        (output) status_msg -> Message stating what is not valid.
        (output) status -> True|False - Any of the configuration files invalid.

    """

    status = True
    status_msg = []

    for SVR in SERVERS:

        status, err_msg = gen_libs.chk_crt_file(SVR.extra_def_file)

        if not status:
            status_msg.append("%s" % (err_msg))

        if SVR.extra_def_file and not status:

            status_msg.append("%s:  %s is missing." % (SVR.name,
                                                       SVR.extra_def_file))
            status = False

    return status, status_msg


def is_logs_synced(MST, SLV):

    """Function:  is_logs_synced

    Description:  Checks to see if the Master binary log file name and log
        position match that the Slave's Relay log file name and log position.

    Arguments:
        (input) MST -> Master class instance.
        (input) SLV -> Slave class instance.
        (output) True or False -> True is return if logs are in sync.

    """

    is_synced = True

    if MST.gtid_mode and SLV.gtid_mode:
        if MST.exe_gtid != SLV.exe_gtid:
            is_synced = False

    # Non-GTID server.
    else:
        if MST.file != SLV.relay_mst_log or MST.pos != SLV.exec_mst_pos:
            is_synced = False

    return is_synced


def is_rep_delay(MST, SLV, opt):

    """Function:  is_rep_delay

    Description:  Checks to see if there is a delay in the replication system.
        There is an IO and SQL check, determined by arguments.  Will
        determine whether to use GTIDs or the file and log positions
        based on the GTID settings in Master and Slave.

    Arguments:
        (input) MST -> Master class instance.
        (input) SLV -> Slave class instance.
        (input) opt -> IO or SQL - Determines which thread to check.
        (output) Return True if delay detected, False if no delay.

    """

    is_delay = False

    #  IO thread check.
    if opt == "IO":

        if MST.gtid_mode and SLV.gtid_mode:
            if MST.exe_gtid != SLV.retrieved_gtid:
                is_delay = True

        else:
            if MST.file != SLV.mst_log or MST.pos != SLV.mst_read_pos:
                is_delay = True

    # Assume SQL thread check.
    else:
        if MST.gtid_mode and SLV.gtid_mode:
            if MST.exe_gtid != SLV.exe_gtid:
                is_delay = True

        else:
            if MST.file != SLV.relay_mst_log or MST.pos != SLV.exec_mst_pos:
                is_delay = True

    return is_delay


def optimize_tbl(SERVER, db, tbl, res_set="all", **kwargs):

    """Function:  optimize_tbl

    Description:  Runs a check table command against a table.

    Arguments:
        (input) SERVER -> Server instance.
        (input) db -> Database name.
        (input) tbl -> Table name.
        (input) res_set -> row|all - Returning result set format.
        (output) Return check table results.

    """

    # Must have back ticks around names if they have special characters.
    sql_cmd = "optimize table `" + db + "`.`" + tbl + "`"

    return SERVER.sql(sql_cmd, res_set)


def purge_bin_logs(SERVER, prg_type, cutoff):

    """Function:  purge_bin_logs

    Description:  Runs the purge binary logs command.

    Arguments:
        (input) SERVER -> Server instance.
        (input) prg_type -> Purge type:  BEFORE or TO.
        (input) cutoff -> Depends on the prg_type.
            => BEFORE -> cutoff will be a date and time.
            => TO     -> cutoff will be a binary log file name.

    """

    sql_cmd = "purge binary logs " + prg_type + " '" + cutoff + "'"
    SERVER.sql(sql_cmd)


def reset_master(SERVER):

    """Function:  reset_master

    Description:  Run reset master command.

    Arguments:
        (input) SERVER -> Server instance.

    """

    SERVER.sql("reset master")


def reset_slave(SERVER):

    """Function:  reset_slave

    Description:  Clear replication configuration on the slave.

    Arguments:
        (input) SERVER -> Server instance.

    """

    SERVER.sql("reset slave all")


def select_wait_until(SERVER, gtid_pos, timeout=0, res_set="row"):

    """Function:  select_wait_until

    Description:  Wait to return until GTID position is reached or if timeout
        is reached, which ever comes first.

    Arguments:
        (input) SERVER -> Server instance.
        (input) gtid_pos -> GTID Position.
        (input) timeout -> Number of seconds before exiting command.
            Warning:  If set to 0 (zero), will wait indefinitely.
        (input) res_set -> row or all - Returning result set.
        (output) -1, 0, >0 - Return status of command.
            -1: Timeout reached and did not reach GTID position.
            0:  Already at GTID position, no transactions processed.
            >0: Reached GTID position, number of transactions processed.

    """

    return SERVER.sql("select wait_until_sql_thread_after_gtids(%s, %s)",
                      res_set, (gtid_pos, timeout))


def start_slave_until(SLV, log_file=None, log_pos=None, **kwargs):

    """Function:  start_slave_until

    Description:  Starts the slave with the until option to run it until a
        specified file and position or specified GTID position, also
        includes the 'before' and 'after' option for the GTID syntax.

    Arguments:
        (input) SLV -> Slave class instance.
        (input) log_file -> Binary log file name.
        (input) log_pos -> Binary log position.
        (input) **kwargs:
            gtid -> GTID position
            stop_pos -> 'before' or 'after' option in syntax. Default: 'before'
        (output) err_flag -> True|False - if an error has occured.
        (output) err_msg -> Error message.

    """

    err_flag = False
    err_msg = None
    gtid = kwargs.get("gtid", None)
    stop_pos = kwargs.get("stop_pos", "before")
    start_slv = """start slave until """

    # Non-GTID MySQL.
    if log_file and log_pos:
        start_slave_until = start_slv + \
            """master_log_file=%s, master_log_pos=%s"""
        master_pos_wait = """select master_pos_wait(%s, %s)"""

        SLV.sql(start_slave_until, "", (log_file, log_pos))
        SLV.sql(master_pos_wait, "", (log_file, log_pos))

    # GTID MySQL.
    elif SLV.gtid_mode and gtid:
        start_slave_until = start_slv + """sql_""" + stop_pos + """_gtids=%s"""

        SLV.sql(start_slave_until, "", (gtid))

    else:
        err_flag = True
        err_msg = "One of the arguments is missing."
        return err_flag, err_msg

    return err_flag, err_msg


def switch_to_master(MST, SLV, timeout=0):

    """Function:  switch_to_master

    Description:  Waits until the Slave relay log is empty and then changes the
        Slave to the new Master.

    Arguments:
        (input) MST -> Master class instance.
        (input) SLV -> Slave class instance.
        (input) timeout -> Number of seconds to wait for return.
            NOTE:  0 (zero) means wait indefinitely.
        (output) -1, 0, >0 - Return status of command.
            -1: Timeout reached and did not reach GTID position.
            0:  Already at GTID position, no transactions processed.
            >0: Reached GTID position, number of transactions processed.

    """

    # Wait for relay log to empty.
    SLV.upd_gtid_pos()
    status_flag = select_wait_until(SLV, SLV.retrieved_gtidset, timeout)

    if status_flag >= 0:
        mysql_class.slave_stop(SLV)
        change_master_to(MST, SLV)
        mysql_class.slave_start(SLV)

    return status_flag


def sync_delay(MST, SLV, opt):

    """Function:  sync_delay

    Description:  Checks to see if there is an IO or SQL delay between the
        master and the slave.  Calls functions to sync up between the master
        and slave.

    Arguments:
        (input) MST -> Master class instance.
        (input) SLV -> Slave class instance.
        (input) opt -> IO or SQL - Determines which thread to check.

    """

    if is_rep_delay(MST, SLV, opt):

        # IO check.
        if opt == "IO":

            # Start slave until requested position for GTID or non-GTID.
            if MST.gtid_mode and SLV.gtid_mode:
                # By default using the "sql_after_gtid" option.
                err_flag, err_msg = start_slave_until(SLV, gtid=MST.exe_gtid,
                                                      stop_pos="after")

                if err_flag:
                    print("Error: {0}" % (err_msg))

            else:
                err_flag, err_msg = start_slave_until(SLV, MST.file, MST.pos)

                if err_flag:
                    print("Error: {0}" % (err_msg))

        print("Master: {0}\tFile: {1}, Position: {2}".
              format(MST.name, MST.file, MST.pos))

        if MST.gtid_mode:
            print("\tGTID: {0}".format(MST.exe_gtid))

        # Wait until position is reached for GTID or non-GTID.
        if MST.gtid_mode and SLV.gtid_mode:
            wait_until(SLV, opt, gtid=MST.exe_gtid)

        else:
            wait_until(SLV, opt, MST.file, MST.pos)

        # IO check.
        if opt == "IO":
            SLV.stop_slave()


def sync_rep_slv(MST, SLV, **kwargs):

    """Function:  sync_rep_slv

    Description:  Syncs up the slave to the master, returns an error if the
        sync is not completed.

    Arguments:
        (input) MST -> Master class instance.
        (input) SLV -> Slave class instance.
        (output) err_flag -> True|False - if an error has occurred.
        (output) err_msg -> Error message.

    """

    option = ["IO", "SQL"]
    err_flag = False
    err_msg = None

    # Slave isn't under master.
    if SLV.mst_id != MST.server_id:
        err_flag = True
        err_msg = "Error:  Slave's Master ID %s doesn't match Master ID %s." \
                  % (SLV.mst_id, MST.server_id)

        return err_flag, err_msg

    if SLV.is_slv_running():
        chg_slv_state([SLV], "stop")

    # Master and slave are not synced.
    if not is_logs_synced(MST, SLV):

        for opt in option:
            sync_delay(MST, SLV, opt)

            if not is_logs_synced(MST, SLV):
                err_flag = True
                err_msg = "Error:  Server %s not in sync with master." % (SLV)

    return err_flag, err_msg


def wait_until(SLV, opt, log_file=None, log_pos=None, **kwargs):

    """Function:  wait_until

    Description:  Determines whether to run an IO or SQL check in the Slave
        database server.

    Arguments:
        (input) SLV -> Slave class instance.
        (input) opt -> IO or SQL - Determines which thread to check.
        (input) log_file -> Master binary log file name.
        (input) log_pos -> Master binary log position.
        (input) **kwargs:
            gtid -> GTID position.

    """

    gtid = kwargs.get("gtid", None)
    SLV.upd_slv_status()

    if opt == "IO":
        _io_chk(SLV, gtid, log_file, log_pos)

    else:
        _sql_chk(SLV, gtid, log_file, log_pos)


def _io_chk(SLV, gtid, log_file, log_pos, **kwargs):

    """Function:  _io_chk

    Description:  Checks the slave's IO thread to to see if the server has
        reached the master's log file and position (non-GTID enabled) or the
        GTID position (GTID enabled).  Loops until the process completes or
        manual interruption.

    Arguments:
        (input) SLV -> Slave class instance.
        (input) gtid -> GTID position.
        (input) log_file -> Master's binary log file name.
        (input) log_pos -> Master's binary log position.

    """

    while True:
        if SLV.gtid_mode:
            print("Slave:  {0}\t Retrieved GTID: {1}".
                  format(SLV.name, SLV.retrieved_gtid))

            if SLV.retrieved_gtid == gtid:
                return

        else:
            print("Slave:  {0}\tFile: {1}, Position: {2}".
                  format(SLV.name, SLV.mst_log, SLV.mst_read_pos))

            if SLV.mst_log == log_file and SLV.mst_read_pos == log_pos:
                return

        time.sleep(3)
        SLV.upd_slv_status()


def _sql_chk(SLV, gtid, log_file, log_pos, **kwargs):

    """Function:  _sql_chk

    Description:  Checks the slave's SQL thread to to see if the server has
        reached the master's log file and position (non-GTID enabled) or the
        GTID position (GTID enabled).  Loops until the process completes or
        manual interruption.

    Arguments:
        (input) SLV -> Slave class instance.
        (input) gtid -> GTID position.
        (input) log_file -> Master's binary log file name.
        (input) log_pos -> Master's binary log position.

    """

    while True:
        if SLV.gtid_mode:
            print("Slave:  {0}\tGTID: {1}".format(SLV.name, SLV.exe_gtid))

            if SLV.exe_gtid == gtid:
                return

        else:
            print("Slave: {0}\tcurrent file: {1}, current position: {2}".
                  format(SLV.name, SLV.relay_mst_log, SLV.exec_mst_pos))

            if SLV.relay_mst_log == log_file and SLV.exec_mst_pos == log_pos:
                return

        time.sleep(3)
        SLV.upd_slv_status()
