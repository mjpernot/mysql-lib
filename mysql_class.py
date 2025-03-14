# Classification (U)

"""Program:  mysql_class.py

    Description:  Class holding MySQL server definitions.

    Functions:
        fetch_global_var
        fetch_sys_var
        flush_logs
        show_master_stat
        show_slave_hosts
        show_slave_stat
        slave_start
        slave_stop

    Classes:
        Position
        GTIDSet
        Server
            Rep
                MasterRep
                SlaveRep

"""

# Libraries and Global Variables

# Standard
import copy
import collections
import mysql.connector

# Local
try:
    from .lib import gen_libs
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import version

__version__ = version.__version__

# Global
SHOW = "show "


def fetch_global_var(server, var):

    """Function:  fetch_global_var

    Description:  Returns the value for a global variable.

    Arguments:
        (input) server -> Server instance
        (input) var -> Global variable name
        (output) Variable returned in dictionary format (e.g. {name: value})

    """

    cmd = "show global status like %s"

    return server.vert_sql(cmd, (var,))


def fetch_sys_var(server, var, **kwargs):

    """Function:  fetch_sys_var

    Description:  Returns the value for a variable.  Can set the level at
        which to return the variable from:  global|session.
        NOTE:  Will use 'session' level by default.

    Arguments:
        (input) server -> Server instance
        (input) var -> Variable name
        (Input) **kwargs:
            level - global|session - level at which command will run
        (output) Variable returned in dictionary format (e.g. {name: value})

    """

    global SHOW                                     # pylint:disable=W0602

    cmd = SHOW + kwargs.get("level", "session") + " variables like %s"

    return server.vert_sql(cmd, (var,))


def flush_logs(server):

    """Function:  flush_logs

    Description:  Run the MySQL 'flush logs' command.

    Arguments:
        (input) server -> Server instance

    """

    server.cmd_sql("flush logs")


def show_master_stat(server):

    """Function:  show_master_stat

    Description:  Return results of the 'show master status' command.

    Arguments:
        (input) server -> Server instance
        (output) Results of command in dictionary format

    """

    return server.col_sql("show master status")


def show_slave_hosts(server):

    """Function:  show_slave_hosts

    Description:  Return the output of the 'show slave hosts' command.

    Arguments:
        (input) server -> Server instance
        (output) Results of command in dictionary format

    """

    global SHOW                                     # pylint:disable=W0602

    # Semantic change in MySQL 8.0.22
    slaves = "replicas" if server.version >= (8, 0, 22) else "slave hosts"

    return server.col_sql(SHOW + slaves)


def show_slave_stat(server):

    """Function:  show_slave_stat

    Description:  Return the output of the 'show slave status' command.

    Arguments:
        (input) server -> Server instance
        (output) Results of command in dictionary format

    """

    global SHOW                                     # pylint:disable=W0602

    # Semantic change in MySQL 8.0.22
    slave = "replica" if server.version >= (8, 0, 22) else "slave"

    return server.col_sql(SHOW + slave + " status")


def slave_start(server):

    """Function:  slave_start

    Description:  Starts the slave thread.

    Arguments:
        (input) server -> Server instance

    """

    # Semantic change in MySQL 8.0.22
    slave = "replica" if server.version >= (8, 0, 22) else "slave"

    server.cmd_sql("start " + slave)


def slave_stop(server):

    """Function:  slave_stop

    Description:  Stops the slave thread.

    Arguments:
        (input) server -> Server instance

    """

    # Semantic change in MySQL 8.0.22
    slave = "replica" if server.version >= (8, 0, 22) else "slave"

    server.cmd_sql("stop " + slave)


class Position(collections.namedtuple("Position", "file, pos")):

    """Class:  Position

    Description:  Class which holds a binary log position for a specific
        server.

    Methods:
        cmp

    """

    def cmp(self, other):

        """Method: cmp

        Description:  Compare two positions lexicographically.  Returns -1, 0
            or 1.
            Return values:
                -1: self is before other
                0: self and other are equal
                1: self is after other

        Arguments:
            (input) other -> Second server to be compared with

        """

        return (self > other) - (self < other)


def compare_sets(lhs, rhs):

    """Method:  compare_sets

    Description:  Compare two GTID sets.  Return a tuple (lhs, rhs) where lhs
        is a boolean indication that the left hand side had at least one more
        item than the right hand side and vice verse.

    Arguments:
        (input) lhs -> Left hand side set
        (input) rhs -> Right hand side set
        (output) lcheck -> True | False for Left side check
        (output) rcheck -> True | False for Right side check

    """

    lcheck, rcheck = False, False

    # Create a union of the lhs and rhs for comparsion.
    both = copy.deepcopy(lhs)
    both.union(rhs)

    for uuid, rngs in list(both.gtids.items()):
        # They are incomparable.
        if lcheck and rcheck:
            return lcheck, rcheck

        if _inner_compare(lhs, uuid, rngs):
            rcheck = True

        if _inner_compare(rhs, uuid, rngs):
            lcheck = True

    return lcheck, rcheck


def _inner_compare(gtid_set, uuid, rngs):

    """Method:  inner_compare

    Description:  Checks to see if the UUID is in the GTID Set passed
        to the method.

    Arguments:
        (input) gtid_set -> GTIDSet instance
        (input) uuid -> Universal Unqiue Identifier
        (input) rngs -> Set of ranges
        (output) -> True|False on whether UUID was detected

    """

    # UUID not in lhs ==> right hand side has more
    if uuid not in gtid_set.gtids:
        return True

    for rng1, rng2 in zip(rngs, gtid_set.gtids[uuid]):
        if rng1 != rng2:
            return True

    return False


class GTIDSet():

    """Class:  GTIDSet

    Description:  Class which is a representation of a GTID set within the
        MySQL database.  The GTIDSet object is used to contain and process
        GTIDs.  The basic methods and attributes include comparing two
        GTIDs using the rich comparsion operator methods, combine
        GTID sets and converting GTIDs to strings.

    Methods:
        __init__
        __str__
        union
        __lt__
        __le__
        __eq__
        __ne__
        __ge__
        __gt__
        __or__

    """

    def __init__(self, obj):

        """Method:  __init__

        Description:  Initialization an instance of the GTIDSet class.

        Arguments:
            (input) obj -> Raw GTID name and range

        """

        gtids = {}

        # Convert to string to parse
        if not isinstance(obj, str):
            obj = str(obj)

        # Parse string and construct a GTID set.
        for uuid_set in obj.split(","):
            parts = uuid_set.split(":")

            uuid = parts.pop(0)

            if len(parts) == 0 or not parts[0]:
                raise ValueError("At least one range has to be provided.")

            rngs = [tuple(int(x) for x in part.split("-")) for part in parts]

            for rng in rngs:
                if len(rng) > 2 or len(rng) == 2 and int(rng[0]) > int(rng[1]):
                    rng2 = "-".join(str(i) for i in rng)
                    raise ValueError(
                        f"Range {rng2} in '{rng}' is not a valid range.")

            gtids[uuid] = gen_libs.normalize(rngs)

        self.gtids = gtids

    def __str__(self):

        """Method:  __str__

        Description:  Combines and converts to a string all parts of the class.

        Arguments:
            (output) -> String of the GTID class combined together

        """

        sets = []

        for uuid, rngs in sorted(self.gtids.items()):
            uuid_set = ":".join([str(uuid)] + ["-".join(str(i) for i in rng)
                                               for rng in rngs])

            sets.append(uuid_set)

        return ",".join(sets)

    def union(self, other):

        """Method:  union

        Description:  Compute the union of this GTID set and the GTID set in
            the other.  The update of the GTID set is done in-place, so if you
            want to compute the union of two sets 'lhs' and 'rhs' you have to
            do something like:
                data = copy.deepcopy(lhs)
                data.union(rhs)

        Arguments:
            (input) other -> Second GTID set

        """

        # If it wasn't already a GTIDSet, try to make it one.
        if not isinstance(other, GTIDSet):
            other = GTIDSet(other)

        gtids = self.gtids

        # Parse the other GTID set and combine with the first GTID set.
        for uuid, rngs in list(other.gtids.items()):
            if uuid not in gtids:
                gtids[uuid] = rngs

            else:
                gtids[uuid] = gen_libs.normalize(gtids[uuid] + rngs)

        self.gtids = gtids

    def __lt__(self, other):

        """Method:  __lt__

        Description:  Is first GTID set less than second GTID set.

        Arguments:
            (output) -> True | False

        """

        lhs, rhs = compare_sets(self, other)
        return not lhs and rhs

    def __le__(self, other):

        """Method:  __le__

        Description:  Is first GTID set less than or equal to second GTID set.

        Arguments:
            (output) -> True | False

        """

        lhs, _ = compare_sets(self, other)
        return not lhs

    def __eq__(self, other):

        """Method:  __eq__

        Description:  Is first GTID set equal to second GTID set.

        Arguments:
            (output) -> True | False

        """

        lhs, rhs = compare_sets(self, other)

        return not (lhs or rhs)

    def __ne__(self, other):

        """Method:  __ne__

        Description:  Is first GTID set not equal to second GTID set.

        Arguments:
            (output) -> True | False

        """

        return not self.__eq__(other)

    def __ge__(self, other):

        """Method:  __ge__

        Description:  Is first GTID set greater than or equal to second GTID
            set.

        Arguments:
            (output) -> True | False

        """

        return other.__le__(self)

    def __gt__(self, other):

        """Method:  __gt__

        Description:  Is first GTID set greater than second GTID set.

        Arguments:
            (output) -> True | False

        """

        return other.__lt__(self)

    def __or__(self, other):

        """Method:  __or__

        Description:  Return first set (self) with elements added from second
            set (other).

        Arguments:
            (output) result -> First set with elements from second set

        """

        data = copy.deepcopy(self)
        data.union(other)

        return data


class Server():                                 # pylint:disable=R0902,R0904

    """Class:  Server

    Description:  Class which is a representation of a MySQL server.  A server
        object is used as a proxy for operating with the server.  The
        basic methods and attributes include connecting to the server
        and executing SQL statements.

    Methods:
        __init__
        set_srv_binlog_crc
        set_srv_gtid
        upd_srv_perf
        upd_srv_stat
        upd_mst_rep_stat
        upd_slv_rep_stat
        fetch_mst_rep_cfg
        fetch_slv_rep_cfg
        upd_log_stats
        flush_logs
        fetch_log
        connect
        disconnect
        sql
        cmd_sql
        col_sql
        vert_sql
        is_connected
        reconnect
        chg_db
        get_name
        set_pass_config
        setup_ssl
        set_ssl_config
        set_tls_config

    """

    def __init__(                               # pylint:disable=R0915,R0913
            self, name, server_id, sql_user, sql_pass, os_type, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Server class.

        Arguments:
            (input) name -> Name of the MySQL server
            (input) server_id -> Server's ID
            (input) sql_user -> SQL user's name
            (input) sql_pass -> SQL user's pswd
            (input) os_type -> Machine operating system type class instance
            (input) kwargs:
                extra_def_file -> Location of extra defaults file
                host -> Host name or IP of server
                port -> Port for MySQL
                defaults_file -> Location of my.cnf file
                ssl_client_ca -> SSL certificate authority file
                ssl_client_key -> SSL X.509 key file
                ssl_client_cert -> SSL X.509 certificate file
                ssl_client_flag -> SSL client flag option
                ssl_disabled -> True|False - Disable SSL
                ssl_verify_id -> True|False - Validate the destination host
                ssl_verify_cert -> True|False - Validate the CA certification
                tls_versions -> List of TLS versions

        """

        self.name = name
        self.server_id = server_id
        self.sql_user = sql_user
        self.machine = os_type
        self.host = kwargs.get("host", "localhost")
        self.port = kwargs.get("port", 3306)
        self.defaults_file = kwargs.get("defaults_file",
                                        self.machine.defaults_file)
        self.extra_def_file = kwargs.get("extra_def_file", None)
        self.config = {}

        # Passwd configuration setup
        self.sql_pass = sql_pass
        self.set_pass_config()

        # SSL configuration settings
        self.ssl_client_ca = kwargs.get("ssl_client_ca", None)
        self.ssl_client_key = kwargs.get("ssl_client_key", None)
        self.ssl_client_cert = kwargs.get("ssl_client_cert", None)
        self.ssl_client_flag = kwargs.get("ssl_client_flag",
                                          mysql.connector.ClientFlag.SSL)
        self.ssl_disabled = kwargs.get("ssl_disabled", False)
        self.ssl_verify_id = kwargs.get("ssl_verify_id", False)
        self.ssl_verify_cert = kwargs.get("ssl_verify_cert", False)
        self.set_ssl_config()

        # TLS configuration settings
        self.tls_versions = kwargs.get("tls_versions", [])
        self.set_tls_config()

        # SQL connection handler.
        self.conn = None
        self.conn_msg = None

        # Binary log information.
        self.pos = None
        self.do_db = None
        self.file = None
        self.ign_db = None

        # Master rep config settings.
        self.log_bin = None
        self.sync_log = None
        self.innodb_flush = None
        self.innodb_xa = None
        self.log_format = None

        # Slave rep config settings.
        #   Note:  log_bin is also part of Slave, but is in the Master area.
        self.read_only = None
        self.log_slv_upd = None
        self.sync_mst = None
        self.sync_relay = None
        self.sync_rly_info = None

        # Memory & status configuration
        self.buf_size = None
        self.indb_buf = None
        self.indb_log_buf = None
        self.qry_cache = None
        self.read_buf = None
        self.read_rnd_buf = None
        self.sort_buf = None
        self.join_buf = None
        self.thrd_stack = None
        self.max_pkt = None
        self.net_buf = None
        self.max_conn = None
        self.max_heap_tbl = None
        self.tmp_tbl = None
        self.cur_conn = None
        self.uptime = None
        self.days_up = None
        self.base_mem = None
        self.thr_mem = None
        self.tmp_tbl_size = None
        self.max_mem_usage = None
        self.cur_mem_usage = None
        self.prct_conn = None
        self.prct_mem = None
        self.cur_mem_mb = None
        self.max_mem_mb = None

        # Performace statistics.
        self.indb_buf_data = None
        self.indb_buf_tot = None
        self.indb_buf_data_pct = None
        self.indb_buf_drty = None
        self.max_use_conn = None
        self.uptime_flush = None
        self.binlog_disk = None
        self.binlog_use = None
        self.binlog_tot = None
        self.indb_buf_wait = None
        self.indb_log_wait = None
        self.indb_lock_avg = None
        self.indb_lock_max = None
        self.indb_buf_read = None
        self.indb_buf_reqt = None
        self.indb_buf_read_pct = None
        self.indb_buf_ahd = None
        self.indb_buf_evt = None
        self.indb_buf_evt_pct = None
        self.indb_buf_free = None
        self.indb_buf_write = None
        self.crt_tmp_tbls = None

        # Server's GTID mode.
        self.gtid_mode = None

        # Server's Binlog checksum.
        self.crc = None

        # Server's version
        self.version = None

    def set_srv_binlog_crc(self):

        """Method:  set_srv_binlog_crc

        Description:  Set the Server's Binlog checksum attribute.

        Arguments:

        """

        var = "binlog_checksum"
        data = fetch_sys_var(self, var)

        if data:
            self.crc = data[var]

    def set_srv_gtid(self):

        """Method:  set_srv_gtid

        Description:  Set the Server's GTID mode attribute.

        Arguments:

        """

        var = "gtid_mode"
        data = fetch_sys_var(self, var)
        self.gtid_mode = bool(data) and data[var] == "ON"

    def upd_srv_perf(self):

        """Method:  upd_srv_perf

        Description:  Updates the Server's performance attributes.

        Arguments:

        """

        data = {}

        for item in self.col_sql("show status"):
            data.update({item["Variable_name"]: item["Value"]})

        self.indb_buf_free = int(data["Innodb_buffer_pool_pages_free"])
        self.indb_buf_data = int(data["Innodb_buffer_pool_pages_data"])
        self.indb_buf_tot = int(data["Innodb_buffer_pool_pages_total"])
        self.indb_buf_drty = int(data["Innodb_buffer_pool_pages_dirty"])
        self.max_use_conn = int(data["Max_used_connections"])
        self.uptime_flush = int(data["Uptime_since_flush_status"])
        self.binlog_disk = int(data["Binlog_cache_disk_use"])
        self.binlog_use = int(data["Binlog_cache_use"])
        self.indb_buf_wait = int(data["Innodb_buffer_pool_wait_free"])
        self.indb_log_wait = int(data["Innodb_log_waits"])
        self.indb_lock_avg = int(data["Innodb_row_lock_time_avg"])
        self.indb_lock_max = int(data["Innodb_row_lock_time_max"])
        self.indb_buf_read = int(data["Innodb_buffer_pool_reads"])
        self.indb_buf_reqt = int(data["Innodb_buffer_pool_read_requests"])
        self.indb_buf_evt = int(data["Innodb_buffer_pool_read_ahead_evicted"])
        self.indb_buf_ahd = int(data["Innodb_buffer_pool_read_ahead"])
        self.indb_buf_write = int(data["Innodb_buffer_pool_write_requests"])
        self.crt_tmp_tbls = int(data["Created_tmp_disk_tables"])

        # Percentage of dirty pages in data cache.
        self.indb_buf_data_pct = gen_libs.pct_int(self.indb_buf_data,
                                                  self.indb_buf_tot)

        # Percentage of pool read requests in data cache.
        self.indb_buf_read_pct = gen_libs.pct_int(self.indb_buf_read,
                                                  self.indb_buf_reqt)

        # Percentage of read ahead pages evicted from data cache.
        self.indb_buf_evt_pct = gen_libs.pct_int(self.indb_buf_evt,
                                                 self.indb_buf_ahd)

        # Total binlog cache usage.
        self.binlog_tot = self.binlog_disk + self.binlog_use

    def upd_srv_stat(self):

        """Method:  upd_srv_stat

        Description:  Updates the Server's status attributes.

        Arguments:

        """

        data = {}

        for item in self.col_sql("show global variables"):
            data.update({item["Variable_name"]: item["Value"]})

        self.buf_size = int(data["key_buffer_size"])
        self.indb_buf = int(data["innodb_buffer_pool_size"])
        self.indb_log_buf = int(data["innodb_log_buffer_size"])

        # query_cache_size has been removed in MySQL 8.0
        self.qry_cache = int(data.get("query_cache_size", "0"))

        self.read_buf = int(data["read_buffer_size"])
        self.read_rnd_buf = int(data["read_rnd_buffer_size"])
        self.sort_buf = int(data["sort_buffer_size"])
        self.join_buf = int(data["join_buffer_size"])
        self.thrd_stack = int(data["thread_stack"])
        self.max_pkt = int(data["max_allowed_packet"])
        self.net_buf = int(data["net_buffer_length"])
        self.max_conn = int(data["max_connections"])
        self.max_heap_tbl = int(data["max_heap_table_size"])
        self.tmp_tbl = int(data["tmp_table_size"])
        self.cur_conn = int(fetch_global_var(
            self, "Threads_connected")["Threads_connected"])
        self.uptime = int(fetch_global_var(self, "Uptime")["Uptime"])

        # Data derived from above status values.
        # Days up since last recycle.
        self.days_up = int(self.uptime / 3600.0 / 24)

        # Base memory for database (in bytes).
        self.base_mem = self.buf_size + self.indb_buf + self.indb_log_buf \
            + self.qry_cache

        # Memory per thread connection (in bytes).
        self.thr_mem = self.read_buf + self.read_rnd_buf + self.sort_buf \
            + self.join_buf + self.thrd_stack + self.max_pkt + self.net_buf

        # Set Maximum Memory usage and Current Memory usage.
        self.max_mem_usage = self.base_mem + (self.max_conn * self.thr_mem)
        self.cur_mem_usage = self.base_mem + (self.cur_conn * self.thr_mem)

        # Convert memory from bytes to megabytes.
        self.max_mem_mb = int(float(self.max_mem_usage) / (1024 * 1024))
        self.cur_mem_mb = int(float(self.cur_mem_usage) / (1024 * 1024))

        # Temp table memory size determined by Max Heap Table or Temp Table.
        if self.tmp_tbl > self.max_heap_tbl:
            self.tmp_tbl_size = self.tmp_tbl

        else:
            self.tmp_tbl_size = self.max_heap_tbl

        # Percentage values:
        # Current connections to Max connections
        self.prct_conn = gen_libs.pct_int(self.cur_conn, self.max_conn)

        # Current Memory to Max Memory
        self.prct_mem = gen_libs.pct_int(self.cur_mem_mb, self.max_mem_mb)

    def upd_mst_rep_stat(self):

        """Method:  upd_mst_rep_stat

        Description:  Updates the Master replication setting attributes.

        Arguments:

        """

        self.log_bin = fetch_sys_var(self, "log_bin")["log_bin"]
        self.sync_log = fetch_sys_var(self, "sync_binlog")["sync_binlog"]
        self.innodb_flush = fetch_sys_var(
            self,
            "innodb_flush_log_at_trx_commit")["innodb_flush_log_at_trx_commit"]

        # innodb_support_xa has been removed in MySQL 8.0
        self.innodb_xa = fetch_sys_var(
            self, "innodb_support_xa").get("innodb_support_xa", None)

        self.log_format = fetch_sys_var(self, "binlog_format")["binlog_format"]

    def upd_slv_rep_stat(self):

        """Method:  upd_slv_rep_stat

        Description:  Updates the Slave replication setting attributes.

        Arguments:

        """

        # Semantic change in MySQL 8.0.26
        master = "source" if self.version >= (8, 0, 26) else "master"
        slave = "replica" if self.version >= (8, 0, 26) else "slave"

        self.log_bin = fetch_sys_var(self, "log_bin")["log_bin"]
        self.read_only = fetch_sys_var(self, "read_only")["read_only"]
        self.log_slv_upd = fetch_sys_var(
            self, "log_" + slave + "_updates")["log_" + slave + "_updates"]
        self.sync_mst = fetch_sys_var(
            self, "sync_" + master + "_info")["sync_" + master + "_info"]
        self.sync_relay = fetch_sys_var(
            self, "sync_relay_log")["sync_relay_log"]
        self.sync_rly_info = fetch_sys_var(
            self, "sync_relay_log_info")["sync_relay_log_info"]

    def fetch_mst_rep_cfg(self):

        """Method:  fetch_mst_rep_cfg

        Description:  Returns a dictionary of the Master replication settings.

        Arguments:

        """

        return {"log_bin": self.log_bin,
                "innodb_support_xa": self.innodb_xa,
                "sync_binlog": self.sync_log,
                "binlog_format": self.log_format,
                "innodb_flush_log_at_trx_commit": self.innodb_flush}

    def fetch_slv_rep_cfg(self):

        """Method:  fetch_slv_rep_cfg

        Description:  Returns a dictionary of the Slave replication settings.

        Arguments:

        """

        # Semantic change in MySQL 8.0.26
        master = "source" if self.version >= (8, 0, 26) else "master"
        slave = "replica" if self.version >= (8, 0, 26) else "slave"

        return {"log_bin": self.log_bin,
                "sync_relay_log": self.sync_relay,
                "read_only": self.read_only,
                "sync_" + master + "_info": self.sync_mst,
                "log_" + slave + "_updates": self.log_slv_upd,
                "sync_relay_log_info": self.sync_rly_info}

    def upd_log_stats(self):

        """Method:  upd_log_stats

        Description:  Updates the binary log attributes.

        Arguments:

        """

        data = show_master_stat(self)[0]
        self.pos = data["Position"]
        self.do_db = data["Binlog_Do_DB"]
        self.file = data["File"]
        self.ign_db = data["Binlog_Ignore_DB"]

    def flush_logs(self):

        """Method:  flush_logs

        Description:  Flush the binary log and update the binary log stats.

        Arguments:

        """

        flush_logs(self)
        self.upd_log_stats()

    def fetch_log(self):

        """Method:  fetch_log

        Description:  Returns the binary log file name.

        Arguments:

        """

        if not self.file:
            self.upd_log_stats()

        return self.file

    def connect(self, **kwargs):

        """Method:  connect

        Description:  Sets up a connection to a database.

        Arguments:
            (input) kwargs:
                database -> Name of database to connect to
                silent -> True|False - Print connection error message

        """

        database = kwargs.get("database", "")
        silent = kwargs.get("silent", False)

        if not self.conn:

            try:
                self.conn = mysql.connector.connect(
                    host=self.host, user=self.sql_user, port=self.port,
                    database=database, **self.config)
                self.version = self.conn.get_server_version()
                self.conn_msg = None

            except mysql.connector.Error as err:
                self.conn_msg = \
                    f"Couldn't connect to database. " \
                    f" MySQL error {err.args[0]}: {err.args[1]}"

                if not silent:
                    print(self.conn_msg)

    def disconnect(self):

        """Method:  disconnect

        Description:  Disconnects from a database connection.

        Arguments:

        """

        self.conn.disconnect()

    def sql(self, cmd, res_set="row", params=None):

        """Method:  sql

        Description:  Execute a SQL command in a cursor.  Returns the results
            as either a cursor row iteration or single result set.

        Arguments:
            (input) cmd -> SQL command
            (input) res_set -> row|all - determines the result set
            (input) params -> Position arguments for the SQL command
                NOTE:  Arguments must be in a list or tuple
            (output) Returns cursor row iteration or single result set of data

        """

        cur = self.conn.cursor()
        cur.execute(cmd, params=params)

        if res_set == "row":
            return cur

        return cur.fetchall()

    def cmd_sql(self, cmd):

        """Method:  cmd_sql

        Description:  Execute a command sql and return the status results of
            the command executed.

        Arguments:
            (input) cmd -> Command SQL
            (output) Results of the command executed in dictionary format

        """

        return self.conn.cmd_query(cmd)

    def col_sql(self, cmd):

        """Method:  col_sql

        Description:  Execute a command sql with column definitions.  Takes the
            column definitions from the sql command standard output and
            combines them with the sql command data return to produce a list
            of dictionaries key-values.

        Arguments:
            (input) cmd -> Command SQL
            (output) data -> Results of the sql executed in list format

        """

        data = []
        keys = [str(line[0]) for line in self.conn.cmd_query(cmd)["columns"]]

        for line in self.conn.get_rows()[0]:
            data.append(dict(list(zip(keys, list(line)))))

        return data

    def vert_sql(self, cmd, params=None):

        """Method:  vert_sql

        Description:  Execute a sql query with vertical definitions returns.
            One column contains the column definition and the other column
            contains the value.  Combines the two columns into a dictionary
            format.

        Arguments:
            (input) cmd -> Command SQL
            (input) params -> Position arguments for the SQL command
                NOTE:  Arguments must be in a list or tuple
            (output) data -> Results of the sql executed in list format

        """

        data = {}

        for item in self.sql(cmd, params=params):
            data[item[0]] = item[1]

        return data

    def is_connected(self):

        """Method:  is_connected

        Description:  Checks to see if the connection is still active.

        Arguments:
            (output) -> Returns True|False on whether connection is active

        """

        if self.conn:
            return self.conn.is_connected()

        return False

    def reconnect(self):

        """Method:  reconnect

        Description:  Reconnects to database if connect is non-active.

        Arguments:

        """

        if not self.is_connected():
            self.conn.reconnect()

    def chg_db(self, dbn=None):

        """Method:  chg_db

        Description:  Change to another database.

        Arguments:
            (input) dbn -> Name of database

        """

        if dbn:
            self.conn.database = dbn

    def get_name(self):

        """Method:  get_name

        Description:  Return the server's name.

        Arguments:
            (output) name -> Server Name

        """

        return self.name

    def set_pass_config(self):

        """Method:  set_pass_config

        Description:  Set the SQL passwd config attributes

        Arguments:

        """

        self.config["passwd"] = self.sql_pass

    def setup_ssl(self, ssl_client_ca=None, ssl_client_key=None,
                  ssl_client_cert=None,
                  ssl_client_flag=mysql.connector.ClientFlag.SSL):

        """Method:  setup_ssl

        Description:  Set the ssl attributes and append/update config
            dictionary.

        Arguments:
            (input) ssl_client_ca -> SSL certificate authority file
            (input) ssl_client_key -> SSL X.509 key file
            (input) ssl_client_cert -> SSL X.509 certificate file
            (input) ssl_client_flag -> SSL client flag option

        """

        self.ssl_client_ca = ssl_client_ca
        self.ssl_client_key = ssl_client_key
        self.ssl_client_cert = ssl_client_cert
        self.ssl_client_flag = ssl_client_flag

        if self.ssl_client_ca \
           or (self.ssl_client_key and self.ssl_client_cert):

            self.set_ssl_config()

    def set_ssl_config(self):

        """Method:  set_ssl_config

        Description:  Append SSL attributes to config.

        Arguments:

        """

        if self.ssl_client_ca \
           or (self.ssl_client_key and self.ssl_client_cert):

            self.config["client_flags"] = [self.ssl_client_flag]
            self.config["ssl_disabled"] = self.ssl_disabled
            self.config["ssl_verify_identity"] = self.ssl_verify_id
            self.config["ssl_ca"] = ""

            if self.ssl_client_ca:
                self.config["ssl_ca"] = self.ssl_client_ca
                self.config["ssl_verify_cert"] = self.ssl_verify_cert

            if self.ssl_client_key and self.ssl_client_cert:
                self.config["ssl_key"] = self.ssl_client_key
                self.config["ssl_cert"] = self.ssl_client_cert

    def set_tls_config(self):

        """Method:  set_tls_config

        Description:  Append TLS attributes to config.

        Arguments:

        """

        if self.tls_versions and isinstance(self.tls_versions, list):
            self.config["tls_versions"] = self.tls_versions

        elif self.tls_versions:
            self.config["tls_versions"] = [self.tls_versions]


class Rep(Server):

    """Class:  Rep

    Description:  Class which is a representation of a Replication MySQL
        server.   A replication server object is used as a proxy for operating
        within a MySQL server.  The basic methods and attributes include
        general replication methods.

    Methods:
        __init__
        show_slv_hosts
        stop_slave
        start_slave
        get_serv_id
        get_serv_uuid
        show_slv_state
        fetch_do_db
        fetch_ign_db
        verify_srv_id

    """

    def __init__(                                       # pylint:disable=R0913
            self, name, server_id, sql_user, sql_pass, os_type, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Rep class.

        Arguments:
            (input) name -> Name of the MySQL server.
            (input) server_id -> Server's ID.
            (input) sql_user -> SQL user's name.
            (input) sql_pass -> SQL user's pswd.
            (input) os_type -> Machine operating system type class instance.
            (input) **kwargs:
                extra_def_file -> Location of extra defaults file.
                host -> Host name or IP of server.
                port -> Port for MySQL.
                defaults_file -> Location of my.cnf file.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL X.509 key file.
                ssl_client_cert -> SSL X.509 certificate file.
                ssl_client_flag -> SSL client flag option.
                ssl_disabled -> True|False - Disable SSL.
                ssl_verify_id -> True|False - Validate the destination host.
                ssl_verify_cert -> True|False - Validate the CA certification.

        """

        super(                                          # pylint:disable=R1725
            Rep, self).__init__(
            name, server_id, sql_user, sql_pass, os_type=os_type,
            host=kwargs.get("host", "localhost"),
            port=kwargs.get("port", 3306),
            defaults_file=kwargs.get("defaults_file", os_type.defaults_file),
            extra_def_file=kwargs.get("extra_def_file", None),
            ssl_disabled=kwargs.get("ssl_disabled", False),
            ssl_client_flag=kwargs.get("ssl_client_flag",
                                       mysql.connector.ClientFlag.SSL),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_verify_cert=kwargs.get("ssl_verify_cert", False),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_verify_id=kwargs.get("ssl_verify_id", False),
            ssl_client_key=kwargs.get("ssl_client_key", None))

    def show_slv_hosts(self):

        """Method:  show_slv_hosts

        Description:  Place holder for the show_slv_hosts method in subclass.

        Arguments:

        """

    def stop_slave(self):

        """Method:  stop_slave

        Description:  Place holder for the stop_slave method in subclass.

        Arguments:

        """

    def start_slave(self):

        """Method:  start_slave

        Description:  Place holder for the start_slave method in subclass.

        Arguments:

        """

    def show_slv_state(self):

        """Method:  show_slv_state

        Description:  Place holder for the show_slv_state method in subclass.

        Arguments:

        """

    def get_serv_id(self):

        """Method:  get_serv_id

        Description:  Calls the fetch_sys_var function with the class instance.

        Arguments:
            (output) Return the server's ID.

        """

        var = "server_id"

        return int(fetch_sys_var(self, var)[var])

    def get_serv_uuid(self):

        """Method:  get_serv_uuid

        Description:  Calls the fetch_sys_var function with the class instance.

        Arguments:
            (output) Return the server's UUID.

        """

        var = "server_uuid"

        return fetch_sys_var(self, var)[var]

    def fetch_do_db(self):

        """Method:  fetch_do_db

        Description:  Return a dictionary list of slave's do databases.

        Arguments:
            (output) do_dic -> List of do databases.

        """

        return gen_libs.str_2_list(self.do_db, ",") if self.do_db else []

    def fetch_ign_db(self):

        """Method:  fetch_ign_db

        Description:  Return a dictionary list of slave's ignore databases.

        Arguments:
            (output) ign_dic -> List of ignore databases.

        """

        return gen_libs.str_2_list(self.ign_db, ",") if self.ign_db else []

    def verify_srv_id(self):

        """Method:  verify_srv_id

        Description:  Checks to see if the instance configuration file server
            id matches with the database's server id.

        Arguments:
            (output) True|False -> If config file id and database id match

        """

        return self.server_id == self.get_serv_id()


class MasterRep(Rep):                                   # pylint:disable=R0902

    """Class:  MasterRep

    Description:  Class which is a representation of a Master Replication MySQL
        server.  A master replication server object is used as a proxy
        for operating within a replication MySQL server.  The basic
        methods and attributes include getting slave hosts method.

    Methods:
        __init__
        connect
        show_slv_hosts
        get_log_info
        upd_mst_status

    """

    def __init__(                                       # pylint:disable=R0913
            self, name, server_id, sql_user, sql_pass, os_type, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the MasterRep class.

        Arguments:
            (input) name -> Name of the MySQL server.
            (input) server_id -> Server's ID.
            (input) sql_user -> SQL user's name.
            (input) sql_pass -> SQL user's pswd.
            (input) os_type -> Machine operating system type class instance.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '3306' or port for MySQL.
            (input) defaults_file -> Location of my.cnf file.
            (input) **kwargs:
                extra_def_file -> Location of extra defaults file.
                rep_user -> Replication user name.
                rep_japd -> Replication user pswd.
                host -> Host name or IP of server.
                port -> Port for MySQL.
                defaults_file -> Location of my.cnf file.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL X.509 key file.
                ssl_client_cert -> SSL X.509 certificate file.
                ssl_client_flag -> SSL client flag option.
                ssl_disabled -> True|False - Disable SSL.
                ssl_verify_id -> True|False - Validate the destination host.
                ssl_verify_cert -> True|False - Validate the CA certification.

        """

        super(                                          # pylint:disable=R1725
            MasterRep, self).__init__(
            name, server_id, sql_user, sql_pass, os_type=os_type,
            host=kwargs.get("host", "localhost"),
            port=kwargs.get("port", 3306),
            defaults_file=kwargs.get("defaults_file", os_type.defaults_file),
            extra_def_file=kwargs.get("extra_def_file", None),
            ssl_client_flag=kwargs.get("ssl_client_flag",
                                       mysql.connector.ClientFlag.SSL),
            ssl_disabled=kwargs.get("ssl_disabled", False),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_verify_cert=kwargs.get("ssl_verify_cert", False),
            ssl_client_key=kwargs.get("ssl_client_key", None),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_verify_id=kwargs.get("ssl_verify_id", False))

        self.pos = None
        self.do_db = None
        self.file = None
        self.ign_db = None
        self.exe_gtid = None
        self.rep_user = kwargs.get("rep_user", None)
        self.rep_japd = kwargs.get("rep_japd", None)
        self.slaves = []

    def connect(self, **kwargs):

        """Method:  connect

        Description:  Setups a connection to a replication server and updates
            the replication attributes.

        Arguments:
            (input) **kwargs:
                silent -> True|False - Print connection error message.

        """

        super(                                          # pylint:disable=R1725
            MasterRep, self).connect(silent=kwargs.get("silent", False))

        if self.conn:
            super(MasterRep, self).set_srv_gtid()       # pylint:disable=R1725
            self.upd_mst_status()

    def show_slv_hosts(self):

        """Method:  show_slv_hosts

        Description:  Gets a list of the slave hosts attached to the server.

        Arguments:
            (output) Return output of show_slave_hosts function.

        """

        return show_slave_hosts(self)

    def get_log_info(self):

        """Method:  get_log_info

        Description:  Return's the binary log file name and position.

        Arguments:
            (output) file -> Master binary log file name.
            (output) pos -> Master binary log position.

        """

        return self.file, self.pos

    def upd_mst_status(self):

        """Method:  upd_mst_status

        Description:  Update the status of the master.

        Arguments:

        """

        self.upd_log_stats()
        data = show_master_stat(self)[0]
        self.exe_gtid = data.get("Executed_Gtid_Set", None)
        self.slaves = self.show_slv_hosts()


class SlaveRep(Rep):                                # pylint:disable=R0902

    """Class:  SlaveRep

    Description:  Class which is a representation of a Slave Replication MySQL
        server.  A slave replication server object is used as a proxy
        for operating within a replication MySQL server.  The basic
        methods and attributes include stopping and starting slave methods.

    Methods:
        __init__
        connect
        stop_slave
        start_slave
        show_slv_state
        upd_slv_state
        upd_slv_status
        upd_gtid_pos
        is_slave_up
        is_slv_running
        get_log_info
        get_thr_stat
        get_err_stat
        is_slv_error
        upd_slv_time
        get_time
        get_others
        fetch_do_tbl
        fetch_ign_tbl

    """

    def __init__(                               # pylint:disable=R0915,R0913
            self, name, server_id, sql_user, sql_pass, os_type, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the SlaveRep class.

        Arguments:
            (input) name -> Name of the MySQL server.
            (input) server_id -> Server's ID.
            (input) sql_user -> SQL user's name.
            (input) sql_pass -> SQL user's pswd.
            (input) os_type -> Machine operating system type class instance.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '3306' or port for MySQL.
            (input) defaults_file -> Location of my.cnf file.
            (input) **kwargs:
                extra_def_file -> Location of extra defaults file.
                host -> Host name or IP of server.
                port -> Port for MySQL.
                defaults_file -> Location of my.cnf file.
                rep_user -> Replication user name.
                rep_japd -> Replication user pswd.
                ssl_client_ca -> SSL certificate authority file.
                ssl_client_key -> SSL X.509 key file.
                ssl_client_cert -> SSL X.509 certificate file.
                ssl_client_flag -> SSL client flag option.
                ssl_disabled -> True|False - Disable SSL.
                ssl_verify_id -> True|False - Validate the destination host.
                ssl_verify_cert -> True|False - Validate the CA certification.

        """

        super(                                          # pylint:disable=R1725
            SlaveRep, self).__init__(
            name, server_id, sql_user, sql_pass, os_type=os_type,
            host=kwargs.get("host", "localhost"),
            port=kwargs.get("port", 3306),
            defaults_file=kwargs.get("defaults_file", os_type.defaults_file),
            extra_def_file=kwargs.get("extra_def_file", None),
            ssl_client_flag=kwargs.get("ssl_client_flag",
                                       mysql.connector.ClientFlag.SSL),
            ssl_disabled=kwargs.get("ssl_disabled", False),
            ssl_client_ca=kwargs.get("ssl_client_ca", None),
            ssl_verify_id=kwargs.get("ssl_verify_id", False),
            ssl_client_cert=kwargs.get("ssl_client_cert", None),
            ssl_verify_cert=kwargs.get("ssl_verify_cert", False),
            ssl_client_key=kwargs.get("ssl_client_key", None))

        self.io_state = None
        self.mst_host = None
        self.mst_port = None
        self.conn_retry = None
        self.mst_log = None
        self.mst_read_pos = None
        self.relay_log = None
        self.relay_pos = None
        self.relay_mst_log = None
        self.slv_io = None
        self.slv_sql = None
        self.do_db = None
        self.ign_db = None
        self.do_tbl = None
        self.ign_tbl = None
        self.wild_do_tbl = None
        self.wild_ign_tbl = None
        self.last_err = None
        self.err_msg = None
        self.skip_ctr = None
        self.exec_mst_pos = None
        self.log_space = None
        self.until_cond = None
        self.until_log = None
        self.until_pos = None
        self.ssl_allow = None
        self.ssl_file = None
        self.ssl_path = None
        self.ssl_cert = None
        self.ssl_cipher = None
        self.ssl_key = None
        self.secs_behind = None
        self.ssl_verify = None
        self.io_err = None
        self.io_msg = None
        self.sql_err = None
        self.sql_msg = None
        self.ign_ids = None
        self.mst_id = None
        self.mst_uuid = None
        self.mst_info = None
        self.sql_delay = None
        self.sql_remain = None
        self.slv_sql_state = None
        self.mst_retry = None
        self.mst_bind = None
        self.io_err_time = None
        self.sql_err_time = None
        self.ssl_crl = None
        self.ssl_crl_path = None
        self.retrieved_gtid = None
        self.exe_gtid = None
        self.auto_pos = None
        self.run = None
        self.tmp_tbl = None
        self.tran_retry = None
        self.read_only = None
        self.purged_gtidset = None
        self.retrieved_gtidset = None
        self.exe_gtidset = None
        self.slave_uuid = None

        # Replication connection attributes in replica set.
        self.rep_user = kwargs.get("rep_user", None)
        self.rep_japd = kwargs.get("rep_japd", None)

    def connect(self, **kwargs):

        """Method:  connect

        Description:  Setups a connection to a replication server and updates
            the slave replication attributes.

        Arguments:
            (input) **kwargs:
                silent -> True|False - Print connection error message.

        """

        super(                                          # pylint:disable=R1725
            SlaveRep, self).connect(silent=kwargs.get("silent", False))

        if self.conn:
            super(SlaveRep, self).set_srv_gtid()        # pylint:disable=R1725
            self.upd_slv_status()

    def stop_slave(self):

        """Method:  stop_slave

        Description:  Calls the stop_slave function with the class instance and
            updates appropriate slave replication variables.

        Arguments:
            (output) name -> Server Name.

        """

        # Semantic change in MySQL 8.0.22
        master = "Source" if self.version >= (8, 0, 22) else "Master"
        slave = "Replica" if self.version >= (8, 0, 22) else "Slave"

        slave_stop(self)
        data = show_slave_stat(self)[0]

        self.io_state = data[slave + "_IO_State"]

        try:
            self.secs_behind = int(data["Seconds_Behind_" + master])

        except (ValueError, TypeError):
            self.secs_behind = "null" if self.secs_behind is None \
                or self.secs_behind == "null" else "UNK"

    def start_slave(self):

        """Method:  start_slave

        Description:  Calls the start_slave function with the class instance
            and updates appropriate slave replication variables.

        Arguments:

        """

        # Semantic change in MySQL 8.0.22
        master = "Source" if self.version >= (8, 0, 22) else "Master"
        slave = "Replica" if self.version >= (8, 0, 22) else "Slave"

        slave_start(self)
        data = show_slave_stat(self)[0]

        self.io_state = data[slave + "_IO_State"]

        try:
            self.secs_behind = int(data["Seconds_Behind_" + master])

        except (ValueError, TypeError):
            self.secs_behind = "null" if self.secs_behind is None \
                or self.secs_behind == "null" else "UNK"

    def show_slv_state(self):

        """Method:  show_slv_state

        Description:  Returns current slave status variables.

        Arguments:
            (output) self.io_state -> Slave_IO_State
            (output) self.slv_io -> Slave_IO_Running
            (output) self.slv_sql -> Slave_SQL_Running.

        """

        return self.io_state, self.slv_io, self.slv_sql

    def upd_slv_state(self):

        """Method:  upd_slv_state

        Description:  Updates the slave state status variables.

        Arguments:

        """

        # Semantic change in MySQL 8.0.22
        slave = "Replica" if self.version >= (8, 0, 22) else "Slave"

        data = show_slave_stat(self)[0]
        self.io_state = data[slave + "_IO_State"]
        self.slv_io = data[slave + "_IO_Running"]
        self.slv_sql = data[slave + "_SQL_Running"]

    def upd_slv_status(self):                           # pylint:disable=R0915

        """Method:  upd_slv_status

        Description:  Updates the slave status variables.

        Arguments:

        """

        # Semantic change in MySQL 8.0.22
        master = "Source" if self.version >= (8, 0, 22) else "Master"
        slave = "Replica" if self.version >= (8, 0, 22) else "Slave"

        # Semantic change in MySQL 8.0.26
        slave2 = "replica" if self.version >= (8, 0, 26) else "slave"
        slave3 = "Replica" if self.version >= (8, 0, 26) else "Slave"

        data = show_slave_stat(self)[0]
        self.io_state = data[slave + "_IO_State"]
        self.mst_host = data[master + "_Host"]
        self.mst_port = data[master + "_Port"]
        self.conn_retry = data["Connect_Retry"]
        self.mst_log = data[master + "_Log_File"]
        self.mst_read_pos = data["Read_" + master + "_Log_Pos"]
        self.relay_log = data["Relay_Log_File"]
        self.relay_pos = data["Relay_Log_Pos"]
        self.relay_mst_log = data["Relay_" + master + "_Log_File"]
        self.slv_io = data[slave + "_IO_Running"]
        self.slv_sql = data[slave + "_SQL_Running"]
        self.do_db = data["Replicate_Do_DB"]
        self.ign_db = data["Replicate_Ignore_DB"]
        self.do_tbl = data["Replicate_Do_Table"]
        self.ign_tbl = data["Replicate_Ignore_Table"]
        self.wild_do_tbl = data["Replicate_Wild_Do_Table"]
        self.wild_ign_tbl = data["Replicate_Wild_Ignore_Table"]
        self.last_err = data["Last_Errno"]
        self.err_msg = data["Last_Error"]

        try:
            self.skip_ctr = int(data["Skip_Counter"])

        except ValueError:
            self.skip_ctr = data["Skip_Counter"]

        self.exec_mst_pos = data["Exec_" + master + "_Log_Pos"]
        self.log_space = data["Relay_Log_Space"]
        self.until_cond = data["Until_Condition"]
        self.until_log = data["Until_Log_File"]
        self.until_pos = data["Until_Log_Pos"]
        self.ssl_allow = data[master + "_SSL_Allowed"]
        self.ssl_file = data[master + "_SSL_CA_File"]
        self.ssl_path = data[master + "_SSL_CA_Path"]
        self.ssl_cert = data[master + "_SSL_Cert"]
        self.ssl_cipher = data[master + "_SSL_Cipher"]
        self.ssl_key = data[master + "_SSL_Key"]

        try:
            self.secs_behind = int(data["Seconds_Behind_" + master])

        except (ValueError, TypeError):
            self.secs_behind = "null" if self.secs_behind is None \
                or self.secs_behind == "null" else "UNK"

        self.ssl_verify = data[master + "_SSL_Verify_Server_Cert"]

        try:
            self.io_err = int(data["Last_IO_Errno"])

        except ValueError:
            self.io_err = data["Last_IO_Errno"]

        self.io_msg = data["Last_IO_Error"]

        try:
            self.sql_err = int(data["Last_SQL_Errno"])

        except ValueError:
            self.sql_err = data["Last_SQL_Errno"]

        self.sql_msg = data["Last_SQL_Error"]
        self.ign_ids = data["Replicate_Ignore_Server_Ids"]

        try:
            self.mst_id = int(data[master + "_Server_Id"])

        except ValueError:
            self.mst_id = data[master + "_Server_Id"]

        self.mst_uuid = data.get(master + "_UUID", None)
        self.mst_info = data.get(master + "_Info_File", None)
        self.sql_delay = data.get("SQL_Delay", None)
        self.sql_remain = data.get("SQL_Remaining_Delay", None)
        self.slv_sql_state = data.get(slave + "_SQL_Running_State", None)
        self.mst_retry = data.get(master + "_Retry_Count", None)
        self.mst_bind = data.get(master + "_Bind", None)
        self.io_err_time = data.get("Last_IO_Error_Timestamp", None)
        self.sql_err_time = data.get("Last_SQL_Error_Timestamp", None)
        self.ssl_crl = data.get(master + "_SSL_Crl", None)
        self.ssl_crl_path = data.get(master + "_SSL_Crlpath", None)
        self.retrieved_gtid = data.get("Retrieved_Gtid_Set", None)
        self.exe_gtid = data.get("Executed_Gtid_Set", None)
        self.auto_pos = data.get("Auto_Position", None)

        # tran_retry
        item = "SERVICE_STATE"
        self.run = self.col_sql(
            f"select {item} from"
            f" performance_schema.replication_applier_status")[0][item]
        ctr = "COUNT_TRANSACTIONS_RETRIES"
        self.tran_retry = self.col_sql(
            f"select {ctr} from"
            f" performance_schema.replication_applier_status")[0][ctr]

        self.tmp_tbl = fetch_global_var(
            self, slave2 + "_open_temp_tables")[slave3 + "_open_temp_tables"]
        self.read_only = fetch_sys_var(self, "read_only")["read_only"]

        self.upd_gtid_pos()
        self.slave_uuid = self.get_serv_uuid()

    def upd_gtid_pos(self):

        """Method:  upd_gtid_pos

        Description:  Update the GTIDSet class GTID positions.

        Arguments:

        """

        data = show_slave_stat(self)[0]
        self.retrieved_gtidset = GTIDSet(data.get("Retrieved_Gtid_Set",
                                                  "0:0") or "0:0")
        self.exe_gtidset = GTIDSet(data.get("Executed_Gtid_Set", "0:0") or
                                   "0:0")

        # Handle MySQL 5.5 or 5.6 servers.
        if self.gtid_mode:
            self.purged_gtidset = GTIDSet(fetch_sys_var(
                self, "GTID_PURGED", level="global")["gtid_purged"] or "0:0")

    def is_slave_up(self):

        """Method:  is_slave_up

        Description:  Checks to see if the slave is running.

        Arguments:
            (Output) Returns True | False on slave status.

        """

        self.upd_slv_state()

        return gen_libs.and_is_true(self.slv_io, self.slv_sql)

    def is_slv_running(self):

        """Method:  is_slv_running

        Description:  Checks to see if the slave is running.

        Arguments:
            (Output) Returns True | False on slave status.

        """

        self.upd_slv_status()

        return gen_libs.is_true(self.slv_io) and gen_libs.is_true(self.run) \
            and gen_libs.is_true(self.slv_sql)

    def get_log_info(self):

        """Method:  get_log_info

        Description:  Return the master and relay log file names along with
            their respective log positions.

        Arguments:
            (output) mst_log -> Master_Log_File.
            (output) relay_mst_log -> Relay_Master_Log_File.
            (output) mst_read_pos -> Read_Master_Log_Pos.
            (output) exec_mst_pos -> Exec_Master_Log_Pos.

        """

        return self.mst_log, self.relay_mst_log, self.mst_read_pos, \
            self.exec_mst_pos

    def get_thr_stat(self):

        """Method:  get_thr_stat

        Description:  Return status of the slave's IO and SQL threads.

        Arguments:
            (output) io_state -> Slave_IO_State.
            (output) slv_io -> Slave_IO_Running.
            (output) slv_sql -> Slave_SQL_Running.
            (output) run -> slave_running.

        """

        return self.io_state, self.slv_io, self.slv_sql, self.run

    def get_err_stat(self):

        """Method:  get_err_stat

        Description:  Return the error status of the slave's IO and SQL
            threads.

        Arguments:
            (output) io_err -> Last_IO_Errno.
            (output) sql_err -> Last_SQL_Errno.
            (output) io_msg -> Last_IO_Error.
            (output) sql_msg -> Last_SQL_Error.
            (output) io_err_time -> Last_IO_Error_Timestamp
            (output) sql_err_time -> Last_SQL_Error_Timestamp.

        """

        return self.io_err, self.sql_err, self.io_msg, self.sql_msg, \
            self.io_err_time, self.sql_err_time

    def is_slv_error(self):

        """Method:  is_slv_error

        Description:  Checks for IO and SQL errors detected.

        Arguments:
            (Output) Returns True | False on slave status.

        """

        return self.io_err or self.sql_err

    def upd_slv_time(self):

        """Method:  upd_slv_time

        Description:  Updates the slave's time lag variable.

        Arguments:

        """

        # Semantic change in MySQL 8.0.22
        master = "Source" if self.version >= (8, 0, 22) else "Master"

        data = show_slave_stat(self)[0]

        try:
            self.secs_behind = int(data["Seconds_Behind_" + master])

        except (ValueError, TypeError):
            self.secs_behind = "null" if self.secs_behind is None \
                or self.secs_behind == "null" else "UNK"

    def get_time(self):

        """Method:  get_time

        Description:  Return the slave's time lag variable.

        Arguments:
            (output) secs_behind -> Seconds_Behind_Master.

        """

        return self.secs_behind

    def get_others(self):

        """Method:  get_others

        Description:  Return the slave's skip count, temp table count, and
            retried transaction count variables.

        Arguments:
            (output) skip_ctr -> Skip_Counter
            (output) tmp_tbl -> slave_open_temp_tables
            (output) tran_retry -> slave_retried_transactions.

        """

        return self.skip_ctr, self.tmp_tbl, self.tran_retry

    def fetch_do_tbl(self):

        """Method:  fetch_do_tbl

        Description:  Return a dictionary list of slave's do tables.

        Arguments:
            (output) do_dic -> List of do tables.

        """

        return gen_libs.list_2_dict(
            gen_libs.str_2_list(self.do_tbl, ",")) if self.do_tbl else []

    def fetch_ign_tbl(self):

        """Method:  fetch_ign_tbl

        Description:  Return a dictionary list of slave's ignore tables.

        Arguments:
            (output) ign_dic -> List of ignore tables.

        """

        return gen_libs.list_2_dict(
            gen_libs.str_2_list(self.ign_tbl, ",")) if self.ign_tbl else []
