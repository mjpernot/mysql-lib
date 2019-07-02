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
            Row
            Rep
                MasterRep
                SlaveRep

"""

# Libraries and Global Variables

# Standard
import copy

# Third-party
import mysql.connector
import collections

# Local
import lib.gen_libs as gen_libs
import lib.machine as machine
import lib.errors as errors
import version

__version__ = version.__version__


def fetch_global_var(server, var):

    """Function:  fetch_global_var

    Description:  Returns the value for a global variable.

    Arguments:
        (input) server -> Server instance.
        (input) var -> Global variable name.
        (output) Variable returned in dictionary format (e.g. {name: value}).

    """

    cmd = "show global status like %s"

    return server.vert_sql(cmd, (var,))


def fetch_sys_var(server, var, **kwargs):

    """Function:  fetch_sys_var

    Description:  Returns the value for a variable.  Can set the level at
        which to return the variable from:  global|session.
        NOTE:  Will use 'session' level by default.

    Arguments:
        (input) server -> Server instance.
        (input) var -> Variable name.
        (Input) **kwargs:
            level - global|session - level at which command will run.
        (output) Variable returned in dictionary format (e.g. {name: value}).

    """

    cmd = "show " + kwargs.get("level", "session") + " variables like %s"

    return server.vert_sql(cmd, (var,))


def flush_logs(server):

    """Function:  flush_logs

    Description:  Run the MySQL 'flush logs' command.

    Arguments:
        (input) server -> Server instance.

    """

    server.cmd_sql("flush logs")


def show_master_stat(server):

    """Function:  show_master_stat

    Description:  Return results of the 'show master status' command.

    Arguments:
        (input) server -> Server instance.
        (output) Results of command in dictionary format.

    """

    return server.col_sql("show master status")


def show_slave_hosts(server):

    """Function:  show_slave_hosts

    Description:  Return the output of the 'show slave hosts' command.

    Arguments:
        (input) server -> Server instance.
        (output) Results of command in dictionary format.

    """

    return server.col_sql("show slave hosts")


def show_slave_stat(server):

    """Function:  show_slave_stat

    Description:  Return the output of the 'show slave status' command.

    Arguments:
        (input) server -> Server instance.
        (output) Results of command in dictionary format.

    """

    return server.col_sql("show slave status")


def slave_start(server):

    """Function:  slave_start

    Description:  Starts the slave thread.

    Arguments:
        (input) server -> Server instance.

    """

    server.cmd_sql("start slave")


def slave_stop(server):

    """Function:  slave_stop

    Description:  Stops the slave thread.

    Arguments:
        (input) server -> Server instance.

    """

    server.cmd_sql("stop slave")


class Position(collections.namedtuple("Position", "file, pos")):

    """Class:  Position

    Description:  Class which holds a binary log position for a specific
        server.

    Super-Class:  collections.namedtuple

    Sub-Classes:

    Methods:
        __cmp__

    """

    def __cmp__(self, other):

        """Method:  __cmp__

        Description:  Compare two positions lexicographically.  If the
            positions are from different servers, a ValueError exception will
            be raised.

        Arguments:
            (input) other -> Second server to be compared with.

        """

        return cmp((self.file, self.pos), (other.file, other.pos))


def compare_sets(lhs, rhs):

    """Method:  compare_sets

    Description:  Compare two GTID sets.  Return a tuple (lhs, rhs) where lhs
        is a boolean indication that the left hand side had at least one more
        item than the right hand side and vice verse.

    Arguments:
        (input) lhs -> Left hand side set.
        (input) rhs -> Right hand side set.
        (output) lcheck -> True | False for Left side check.
        (output) rcheck -> True | False for Right side check.

    """

    lcheck, rcheck = False, False

    # Create a union of the lhs and rhs for comparsion.
    both = copy.deepcopy(lhs)
    both.union(rhs)

    for uuid, rngs in both.gtids.items():
        # They are incomparable.
        if lcheck and rcheck:
            return lcheck, rcheck

        def inner_compare(gtid_set):

            """Method:  inner_compare

            Description:  Checks to see if the UUID is in the GTID Set passed
                to the method.

            Arguments:
                (output) -> True | False on whether UUID was detected.

            """

            # UUID not in lhs ==> right hand side has more
            if uuid not in gtid_set.gtids:
                return True

            else:
                for rng1, rng2 in zip(rngs, gtid_set.gtids[uuid]):
                    if rng1 != rng2:
                        return True

            return False

        if inner_compare(lhs):
            rcheck = True

        if inner_compare(rhs):
            lcheck = True

    return lcheck, rcheck


class GTIDSet(object):

    """Class:  GTIDSet

    Description:  Class which is a representation of a GTID set within the
        MySQL database.  The GTIDSet object is used to contain and process
        GTIDs.  The basic methods and attributes include comparing two
        GTIDs using the rich comparsion operator methods, combine
        GTID sets and converting GTIDs to strings.

    Super-Class:  object

    Sub-Classes:

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
            (input) obj -> Raw GTID name and range.

        """

        gtids = {}

        # Convert to string to parse.
        if not isinstance(obj, basestring):
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
                    raise ValueError("Range %s in '%s' is not a valid range."
                                     % ("-".join(str(i) for i in rng), rng))

            gtids[uuid] = gen_libs.normalize(rngs)

        self.gtids = gtids

    def __str__(self):

        """Method:  __str__

        Description:  Combines and converts to a string all parts of the class.

        Arguments:
            (output) -> String of the GTID class combined together.

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
                result = copy.deepcopy(lhs)
                result.union(rhs).

        Arguments:
            (input) other -> Second GTID set.

        """

        # If it wasn't already a GTIDSet, try to make it one.
        if not isinstance(other, GTIDSet):
            other = GTIDSet(other)

        gtids = self.gtids

        # Parse the other GTID set and combine with the first GTID set.
        for uuid, rngs in other.gtids.items():
            if uuid not in gtids:
                gtids[uuid] = rngs

            else:
                gtids[uuid] = gen_libs.normalize(gtids[uuid] + rngs)

        self.gtids = gtids

    def __lt__(self, other):

        """Method:  __lt__

        Description:  Is first GTID set less than second GTID set.

        Arguments:
            (output) -> True | False.

        """

        lhs, rhs = compare_sets(self, other)
        return not lhs and rhs

    def __le__(self, other):

        """Method:  __le__

        Description:  Is first GTID set less than or equal to second GTID set.

        Arguments:
            (output) -> True | False.

        """

        lhs, _ = compare_sets(self, other)
        return not lhs

    def __eq__(self, other):

        """Method:  __eq__

        Description:  Is first GTID set equal to second GTID set.

        Arguments:
            (output) -> True | False.

        """

        lhs, rhs = compare_sets(self, other)

        return not (lhs or rhs)

    def __ne__(self, other):

        """Method:  __ne__

        Description:  Is first GTID set not equal to second GTID set.

        Arguments:
            (output) -> True | False.

        """

        return not self.__eq__(other)

    def __ge__(self, other):

        """Method:  __ge__

        Description:  Is first GTID set greater than or equal to second GTID
            set.

        Arguments:
            (output) -> True | False.

        """

        return other.__le__(self)

    def __gt__(self, other):

        """Method:  __gt__

        Description:  Is first GTID set greater than second GTID set.

        Arguments:
            (output) -> True | False.

        """

        return other.__lt__(self)

    def __or__(self, other):

        """Method:  __or__

        Description:  Return first set (self) with elements added from second
            set (other).

        Arguments:
            (output) result -> First set with elements from second set.

        """

        result = copy.deepcopy(self)
        result.union(other)

        return result


class Server(object):

    """Class:  Server

    Description:  Class which is a representation of a MySQL server.  A server
        object is used as a proxy for operating with the server.  The
        basic methods and attributes include connecting to the server
        and executing SQL statements.

    Super-Class:  object

    Sub-Classes:
        Row

    Methods:
        __init__
        set_srv_binlog_crc
        set_srv_gtid
        upd_srv_perf
        upd_srv_stat
        upd_mst_rep_stat
        upd_slv_rep_stat
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

    """

    class Row(object):

        """Class:  Row

        Description:  A row (iterator) is returned when executing a SQL
            statement.  For statements that return a single row, the object
            will treat it as a row as well.

        Super-Class:  object

        Sub-Classes:

        Methods:
            __init__
            __iter__
            next
            __getitem__
            __str__

        """

        def __init__(self, cursor):

            """Method:  __init__

            Description:  Initialization of an instance of the Row class.

            Arguments:
                (input) cursor -> Cursor handler passed from execute().

            """

            self.cursor = cursor
            self.row = self.cursor.fetchone()

        def __iter__(self):

            """Method:  __iter__

            Description:  Iterator for the returning result set.
                Executed during a loop (e.g. for loop).

            Arguments:
                (output) Returns the instance handler.

            """

            return self

        def next(self):

            """Method:  next

            Description:  Gets the next row or stops the iteration.
                Called directly using server.Row.next(self) command.

            Arguments:
                (output) Returns the row.

            """

            row = self.row

            if row is None:
                raise StopIteration

            else:
                self.row = self.cursor.fetchone()
                return row

        def __getitem__(self, key):

            """Method:  __getitem__

            Description:  Returns the value to a dictionary key.
                Is executed when an instance of a class is referenced as
                an array (e.g. x[i] and x is a class).

            Arguments:
                (input) key -> Key to the dictionary tuple.
                (output) Returns the value of the key in the dictionary.

            """

            if self.row is not None:
                return self.row[key]

            else:
                raise errors.EmptyRowError

        def __str__(self):

            """Method:  __str__

            Description:  Converts the value in the row to a string.
                Executed when the str() function is called.

            Arguments:
                (output) Returns string representation of the values.

            """

            if len(self.row) == 1:
                return str(self.row.values()[0])

            else:
                raise errors.EmptyRowError

    def __init__(self, name, server_id, sql_user, sql_pass, machine,
                 host="localhost", port=3306, defaults_file=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Server class.

        Arguments:
            (input) name -> Name of the MySQL server.
            (input) server_id -> Server's ID.
            (input) sql_user -> SQL user's name.
            (input) sql_pass -> SQL user's password.
            (input) machine -> Operating system.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '3306' or port for MySQL.
            (input) defaults_file -> Location of my.cnf file.
            (input) **kwargs:
                extra_def_file -> Location of extra defaults file.

        """

        if not defaults_file:
            defaults_file = machine.defaults_file

        self.name = name
        self.server_id = server_id
        self.sql_user = sql_user
        self.sql_pass = sql_pass
        self.machine = machine
        self.host = host
        self.port = port
        self.defaults_file = defaults_file
        self.extra_def_file = kwargs.get("extra_def_file", None)

        # SQL connection handler.
        self.conn = None

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
        self.indb_add_pool = None
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
        self.crt_tmp_tbls = None

        # Server's GTID mode.
        self.gtid_mode = None

        # Server's Binlog checksum.
        self.crc = None

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

        if data and data[var] == "ON":
            self.gtid_mode = True

        else:
            self.gtid_mode = False

    def upd_srv_perf(self):

        """Method:  upd_srv_perf

        Description:  Updates the Server's performance attributes.

        Arguments:

        """

        data = {}

        for x in self.col_sql("show status"):
            data.update({x["Variable_name"]: x["Value"]})

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
            None

        """

        data = {}

        for x in self.col_sql("show global variables"):
            data.update({x["Variable_name"]: x["Value"]})

        self.buf_size = int(data["key_buffer_size"])
        self.indb_buf = int(data["innodb_buffer_pool_size"])
        self.indb_add_pool = int(data["innodb_additional_mem_pool_size"])
        self.indb_log_buf = int(data["innodb_log_buffer_size"])
        self.qry_cache = int(data["query_cache_size"])
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
        self.cur_conn = int(fetch_global_var(self,
            "Threads_connected")["Threads_connected"])
        self.uptime = int(fetch_global_var(self, "Uptime")["Uptime"])

        # Data derived from above status values.
        # Days up since last recycle.
        self.days_up = int(float(self.uptime) / 3600 / 24)

        # Base memory for database (in bytes).
        self.base_mem = self.buf_size + self.indb_buf + self.indb_add_pool \
            + self.indb_log_buf + self.qry_cache

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
        self.prct_conn = int(float(self.cur_conn) / self.max_conn * 100)

        # Current Memory to Max Memory
        self.prct_mem = int(float(self.cur_mem_mb) / self.max_mem_mb * 100)

    def upd_mst_rep_stat(self):

        """Method:  upd_mst_rep_stat

        Description:  Updates the Master replication setting attributes.

        Arguments:
            None

        """

        self.log_bin = fetch_sys_var(self, "log_bin")["log_bin"]
        self.sync_log = fetch_sys_var(self, "sync_binlog")["sync_binlog"]
        self.innodb_flush = fetch_sys_var(self,
            "innodb_flush_log_at_trx_commit")["innodb_flush_log_at_trx_commit"]
        self.innodb_xa = fetch_sys_var(self,
            "innodb_support_xa")["innodb_support_xa"]
        self.log_format = fetch_sys_var(self, "binlog_format")["binlog_format"]

    def upd_slv_rep_stat(self):

        """Method:  upd_slv_rep_stat

        Description:  Updates the Slave replication setting attributes.

        Arguments:
            None

        """

        self.log_bin = fetch_sys_var(self, "log_bin")["log_bin"]
        self.read_only = fetch_sys_var(self, "read_only")["read_only"]
        self.log_slv_upd = fetch_sys_var(self,
            "log_slave_updates")["log_slave_updates"]
        self.sync_mst = fetch_sys_var(self,
            "sync_master_info")["sync_master_info"]
        self.sync_relay = fetch_sys_var(self,
            "sync_relay_log")["sync_relay_log"]
        self.sync_rly_info = fetch_sys_var(self,
            "sync_relay_log_info")["sync_relay_log_info"]

    def fetch_mst_rep_cfg(self):

        """Method:  fetch_mst_rep_cfg

        Description:  Returns a dictionary of the Master replication settings.

        Arguments:
            None

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
            None

        """

        return {"log_bin": self.log_bin,
                "sync_relay_log": self.sync_relay,
                "read_only": self.read_only,
                "sync_master_info": self.sync_mst,
                "log_slave_updates": self.log_slv_upd,
                "sync_relay_log_info": self.sync_rly_info}

    def upd_log_stats(self):

        """Method:  upd_log_stats

        Description:  Updates the binary log attributes.

        Arguments:
            None

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
            None

        """

        flush_logs(self)
        self.upd_log_stats()

    def fetch_log(self):

        """Method:  fetch_log

        Description:  Returns the binary log file name.

        Arguments:
            None

        """

        if not self.file:
            self.upd_log_stats()

        return self.file

    def connect(self, database=""):

        """Method:  connect

        Description:  Sets up a connection to a database.

        Arguments:
            (input) database -> Name of database.

        """

        if not self.conn:

            try:
                self.conn = mysql.connector.connect(host=self.host,
                                                    user=self.sql_user,
                                                    passwd=self.sql_pass,
                                                    port=self.port,
                                                    database=database)

            except mysql.connector.Error, err:
                print("Couldn't connect to database.  MySQL error %d: %s" %
                      (err.args[0], err.args[1]))

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
            (input) cmd -> SQL command.
            (input) res_set -> row|all - determines the result set.
            (input) params -> Position arguments for the SQL command.
            (output) Returns cursor row iteration or single result set of data.

        """

        cur = self.conn.cursor()
        cur.execute(cmd, params=params)

        if res_set == "row":
            return cur

        else:
            return cur.fetchall()

    def cmd_sql(self, cmd):

        """Method:  cmd_sql

        Description:  Execute a command sql and return the status results of
            the command executed.

        Arguments:
            (input) cmd -> Command SQL.
            (output) Results of the command executed in dictionary format.

        """

        return self.conn.cmd_query(cmd)

    def col_sql(self, cmd):

        """Method:  col_sql

        Description:  Execute a command sql with column definitions.  Takes the
            column definitions from the sql command standard output and
            combines them with the sql command data return to produce a list
            of dictionaries key-values.

        Arguments:
            (input) cmd -> Command SQL.
            (output) data -> Results of the sql executed in list format.

        """

        data = []
        keys = [str(x[0]) for x in self.conn.cmd_query(cmd)["columns"]]

        for y in self.conn.get_rows()[0]:
            data.append(dict(zip(keys, [x for x in y])))

        return data

    def vert_sql(self, cmd, params=None):

        """Method:  vert_sql

        Description:  Execute a sql query with vertical definitions returns.
            One column contains the column definition and the other column
            contains the value.  Combines the two columns into a dictionary
            format.

        Arguments:
            (input) cmd -> Command SQL.
            (input) params -> Position arguments for the SQL command.
            (output) data -> Results of the sql executed in list format.

        """

        data = {}

        for x in self.sql(cmd, params=params):
            data[x[0]] = x[1]

        return data

    def is_connected(self):

        """Method:  is_connected

        Description:  Checks to see if the connection is still active.

        Arguments:
            (output) -> Returns True|False on whether connection is active.

        """

        return self.conn.is_connected()

    def reconnect(self):

        """Method:  reconnect

        Description:  Reconnects to database if connect is non-active.

        Arguments:

        """

        if not self.is_connected():
            self.conn.reconnect()

    def chg_db(self, db=None):

        """Method:  chg_db

        Description:  Change to another database.

        Arguments:
            (input) db -> Name of database.

        """

        if db:
            self.conn.database = db


class Rep(Server):

    """Class:  Rep

    Description:  Class which is a representation of a Replication MySQL
        server.   A replication server object is used as a proxy for operating
        within a MySQL server.  The basic methods and attributes include
        general replication methods.

    Super-Class:  Server

    Sub-Classes:
        MasterRep
        SlaveRep

    Methods:
        __init__
        show_slv_hosts
        stop_slave
        start_slave
        get_serv_id
        show_slv_state
        fetch_do_db
        fetch_ign_db

    """

    def __init__(self, name, server_id, sql_user, sql_pass, machine,
                 host="localhost", port=3306, defaults_file=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the Rep class.

        Arguments:
            (input) name -> Name of the MySQL server.
            (input) server_id -> Server's ID.
            (input) sql_user -> SQL user's name.
            (input) sql_pass -> SQL user's password.
            (input) machine -> Operating system.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '3306' or port for MySQL.
            (input) defaults_file -> Location of my.cnf file.
            (input) **kwargs:
                extra_def_file -> Location of extra defaults file.

        """

        super(Rep, self).__init__(name, server_id, sql_user, sql_pass, machine,
                                  host, port, defaults_file, **kwargs)

    def show_slv_hosts(self):

        """Method:  show_slv_hosts

        Description:  Place holder for the show_slv_hosts method in subclass.

        Arguments:

        """

        pass

    def stop_slave(self):

        """Method:  stop_slave

        Description:  Place holder for the stop_slave method in subclass.

        Arguments:

        """

        pass

    def start_slave(self):

        """Method:  start_slave

        Description:  Place holder for the start_slave method in subclass.

        Arguments:

        """

        pass

    def show_slv_state(self):

        """Method:  show_slv_state

        Description:  Place holder for the show_slv_state method in subclass.

        Arguments:

        """

        pass

    def get_serv_id(self):

        """Method:  get_serv_id

        Description:  Calls the get_serv_id function with the class instance.

        Arguments:
            (output) Return the server's ID.

        """

        var = "server_id"

        return fetch_sys_var(self, var)[var]

    def fetch_do_db(self):

        """Method:  fetch_do_db

        Description:  Return a dictionary list of slave's do databases.

        Arguments:
            (output) do_dic -> List of do databases.

        """

        do_dic = []

        if self.do_db:
            do_dic = gen_libs.str_2_list(self.do_db, ",")

        return do_dic

    def fetch_ign_db(self):

        """Method:  fetch_ign_db

        Description:  Return a dictionary list of slave's ignore databases.

        Arguments:
            (output) ign_dic -> List of ignore databases.

        """

        ign_dic = []

        if self.ign_db:
            ign_dic = gen_libs.str_2_list(self.ign_db, ",")

        return ign_dic


class MasterRep(Rep):

    """Class:  MasterRep

    Description:  Class which is a representation of a Master Replication MySQL
        server.  A master replication server object is used as a proxy
        for operating within a replication MySQL server.  The basic
        methods and attributes include getting slave hosts method.

    Super-Class:  Rep

    Sub-Classes:

    Methods:
        __init__
        rep_conn
        show_slv_hosts
        get_log_info
        get_name
        upd_mst_status

    """

    def __init__(self, name, server_id, sql_user, sql_pass, machine,
                 host="localhost", port=3306, defaults_file=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the MasterRep class.

        Arguments:
            (input) name -> Name of the MySQL server.
            (input) server_id -> Server's ID.
            (input) sql_user -> SQL user's name.
            (input) sql_pass -> SQL user's password.
            (input) machine -> Operating system.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '3306' or port for MySQL.
            (input) defaults_file -> Location of my.cnf file.
            (input) **kwargs:
                extra_def_file -> Location of extra defaults file.

        """

        super(MasterRep, self).__init__(name, server_id, sql_user, sql_pass,
                                        machine, host, port, defaults_file,
                                        **kwargs)

        self.pos = None
        self.do_db = None
        self.file = None
        self.ign_db = None
        self.exe_gtid = None

    def rep_conn(self):

        """Method:  rep_conn

        Description:  Setups a connection to a replication server and updates
            the replication attributes.

        Arguments:

        """

        super(MasterRep, self).connect()
        super(MasterRep, self).set_srv_gtid()

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

    def get_name(self):

        """Method:  get_name

        Description:  Return the master's server name as listed in config file.

        Arguments:
            (output) name -> Server Name.

        """

        return self.name

    def upd_mst_status(self):

        """Method:  upd_mst_status

        Description:  Update the status of the master.

        Arguments:
            None

        """

        self.upd_log_stats()
        data = show_master_stat(self)[0]
        self.exe_gtid = data.get("Executed_Gtid_Set", None)


class SlaveRep(Rep):

    """Class:  SlaveRep

    Description:  Class which is a representation of a Slave Replication MySQL
        server.  A slave replication server object is used as a proxy
        for operating within a replication MySQL server.  The basic
        methods and attributes include stopping and starting slave methods.

    Super-Class:  Rep

    Sub-Classes:
        None

    Methods:
        __init__
        rep_conn
        stop_slave
        start_slave
        show_slv_state
        upd_slv_state
        upd_slv_status
        upd_gtid_pos
        is_slave_up
        is_slv_running
        get_log_info
        get_name
        get_thr_stat
        get_err_stat
        is_slv_error
        upd_slv_time
        get_time
        get_others
        fetch_do_tbl
        fetch_ign_tbl

    """

    def __init__(self, name, server_id, sql_user, sql_pass, machine,
                 host="localhost", port=3306, defaults_file=None, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the SlaveRep class.

        Arguments:
            (input) name -> Name of the MySQL server.
            (input) server_id -> Server's ID.
            (input) sql_user -> SQL user's name.
            (input) sql_pass -> SQL user's password.
            (input) machine -> Operating system.
            (input) host -> 'localhost' or host name or IP.
            (input) port -> '3306' or port for MySQL.
            (input) defaults_file -> Location of my.cnf file.
            (input) **kwargs:
                extra_def_file -> Location of extra defaults file.

        """

        super(SlaveRep, self).__init__(name, server_id, sql_user, sql_pass,
                                       machine, host, port, defaults_file,
                                       **kwargs)

        self.io_state = None
        self.mst_host = None
        self.mst_port = None
        self.retry = None
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
        self.retry = None
        self.read_only = None
        self.purged_gtidset = None

    def rep_conn(self):

        """Method:  rep_conn

        Description:  Setups a connection to a replication server and updates
            the slave replication attributes.

        Arguments:

        """

        super(SlaveRep, self).connect()
        super(SlaveRep, self).set_srv_gtid()

        self.upd_slv_status()

    def stop_slave(self):

        """Method:  stop_slave

        Description:  Calls the stop_slave function with the class instance and
            updates appropriate slave replication variables.

        Arguments:
            (output) name -> Server Name.

        """

        slave_stop(self)
        results = show_slave_stat(self)[0]

        self.io_state = results["Slave_IO_State"]
        self.secs_behind = results["Seconds_Behind_Master"]

    def start_slave(self):

        """Method:  start_slave

        Description:  Calls the start_slave function with the class instance
            and updates appropriate slave replication variables.

        Arguments:
            None

        """

        slave_start(self)
        results = show_slave_stat(self)[0]

        self.io_state = results["Slave_IO_State"]
        self.secs_behind = results["Seconds_Behind_Master"]

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
            None

        """

        results = show_slave_stat(self)[0]
        self.io_state = results["Slave_IO_State"]
        self.slv_io = results["Slave_IO_Running"]
        self.slv_sql = results["Slave_SQL_Running"]

    def upd_slv_status(self):

        """Method:  upd_slv_status

        Description:  Updates the slave status variables.

        Arguments:
            None

        """

        data = show_slave_stat(self)[0]
        self.io_state = data["Slave_IO_State"]
        self.mst_host = data["Master_Host"]
        self.mst_port = data["Master_Port"]
        self.retry = data["Connect_Retry"]
        self.mst_log = data["Master_Log_File"]
        self.mst_read_pos = data["Read_Master_Log_Pos"]
        self.relay_log = data["Relay_Log_File"]
        self.relay_pos = data["Relay_Log_Pos"]
        self.relay_mst_log = data["Relay_Master_Log_File"]
        self.slv_io = data["Slave_IO_Running"]
        self.slv_sql = data["Slave_SQL_Running"]
        self.do_db = data["Replicate_Do_DB"]
        self.ign_db = data["Replicate_Ignore_DB"]
        self.do_tbl = data["Replicate_Do_Table"]
        self.ign_tbl = data["Replicate_Ignore_Table"]
        self.wild_do_tbl = data["Replicate_Wild_Do_Table"]
        self.wild_ign_tbl = data["Replicate_Wild_Ignore_Table"]
        self.last_err = data["Last_Errno"]
        self.err_msg = data["Last_Error"]
        self.skip_ctr = data["Skip_Counter"]
        self.exec_mst_pos = data["Exec_Master_Log_Pos"]
        self.log_space = data["Relay_Log_Space"]
        self.until_cond = data["Until_Condition"]
        self.until_log = data["Until_Log_File"]
        self.until_pos = data["Until_Log_Pos"]
        self.ssl_allow = data["Master_SSL_Allowed"]
        self.ssl_file = data["Master_SSL_CA_File"]
        self.ssl_path = data["Master_SSL_CA_Path"]
        self.ssl_cert = data["Master_SSL_Cert"]
        self.ssl_cipher = data["Master_SSL_Cipher"]
        self.ssl_key = data["Master_SSL_Key"]
        self.secs_behind = data["Seconds_Behind_Master"]
        self.ssl_verify = data["Master_SSL_Verify_Server_Cert"]
        self.io_err = data["Last_IO_Errno"]
        self.io_msg = data["Last_IO_Error"]
        self.sql_err = data["Last_SQL_Errno"]
        self.sql_msg = data["Last_SQL_Error"]
        self.ign_ids = data["Replicate_Ignore_Server_Ids"]
        self.mst_id = data["Master_Server_Id"]
        self.mst_uuid = data.get("Master_UUID", None)
        self.mst_info = data.get("Master_Info_File", None)
        self.sql_delay = data.get("SQL_Delay", None)
        self.sql_remain = data.get("SQL_Remaining_Delay", None)
        self.slv_sql_state = data.get("Slave_SQL_Running_State", None)
        self.mst_retry = data.get("Master_Retry_Count", None)
        self.mst_bind = data.get("Master_Bind", None)
        self.io_err_time = data.get("Last_IO_Error_Timestamp", None)
        self.sql_err_time = data.get("Last_SQL_Error_Timestamp", None)
        self.ssl_crl = data.get("Master_SSL_Crl", None)
        self.ssl_crl_path = data.get("Master_SSL_Crlpath", None)
        self.retrieved_gtid = data.get("Retrieved_Gtid_Set", None)
        self.exe_gtid = data.get("Executed_Gtid_Set", None)
        self.auto_pos = data.get("Auto_Position", None)

        self.run = fetch_global_var(self, "slave_running")["slave_running"]
        self.tmp_tbl = fetch_global_var(self,
            "slave_open_temp_tables")["slave_open_temp_tables"]
        self.retry = fetch_global_var(self,
            "slave_retried_transactions")["slave_retried_transactions"]
        self.read_only = fetch_sys_var(self, "read_only")["read_only"]

        self.upd_gtid_pos()

    def upd_gtid_pos(self):

        """Method:  upd_gtid_pos

        Description:  Update the GTIDSet class GTID positions.

        Arguments:
            None

        """

        results = show_slave_stat(self)[0]
        self.retrieved_gtidset = GTIDSet(results.get("Retrieved_Gtid_Set",
                                                     "0:0") or "0:0")
        self.exe_gtidset = GTIDSet(results.get("Executed_Gtid_Set", "0:0") or
                                   "0:0")

        # Handle MySQL 5.5 or 5.6 servers.
        if self.gtid_mode:
            self.purged_gtidset = GTIDSet(fetch_sys_var(
                self, "GTID_PURGED", level="global")[0]["Value"] or "0:0")

        else:
            self.purged_gtidset = None

    def is_slave_up(self):

        """Method:  is_slave_up

        Description:  Checks to see if the slave is running.

        Arguments:
            (Output) Returns True | False on slave status.

        """

        return gen_libs.and_is_true(self.slv_io, self.slv_sql)

    def is_slv_running(self):

        """Method:  is_slv_running

        Description:  Checks to see if the slave is running.

        Arguments:
            (Output) Returns True | False on slave status.

        """

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

    def get_name(self):

        """Method:  get_name

        Description:  Return the slave's server name.

        Arguments:
            (output) name -> Server Name.

        """

        return self.name

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
            None

        """

        results = show_slave_stat(self)[0]
        self.secs_behind = results["Seconds_Behind_Master"]

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
            (output) retry -> slave_retried_transactions.

        """

        return self.skip_ctr, self.tmp_tbl, self.retry

    def fetch_do_tbl(self):

        """Method:  fetch_do_tbl

        Description:  Return a dictionary list of slave's do tables.

        Arguments:
            (output) do_dic -> List of do tables.

        """

        do_dic = []

        if self.do_tbl:
            do_dic = gen_libs.list_2_dict(gen_libs.str_2_list(self.do_tbl,
                                                              ","))

        return do_dic

    def fetch_ign_tbl(self):

        """Method:  fetch_ign_tbl

        Description:  Return a dictionary list of slave's ignore tables.

        Arguments:
            (output) ign_dic -> List of ignore tables.

        """

        ign_dic = []

        if self.ign_tbl:
            ign_dic = gen_libs.list_2_dict(gen_libs.str_2_list(self.ign_tbl,
                                                               ","))

        return ign_dic
