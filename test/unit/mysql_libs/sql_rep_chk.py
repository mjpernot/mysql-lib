# Classification (U)

"""Program:  sql_rep_chk.py

    Description:  Unit testing of sql_rep_chk in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/sql_rep_chk.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_libs                           # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class MasterRep():                          # pylint:disable=R0903

    """Class:  MasterRep

    Description:  Class stub holder for mysql_class.MasterRep class.

    Methods:
        __init__

    """

    def __init__(self, gtid_mode, exe_gtid, filename, pos):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = gtid_mode
        self.exe_gtid = exe_gtid
        self.file = filename
        self.pos = pos


class SlaveRep():                           # pylint:disable=R0903

    """Class:  SlaveRep

    Description:  Class stub holder for mysql_class.SlaveRep class.

    Methods:
        __init__

    """

    def __init__(                           # pylint:disable=R0913
            self, gtid_mode, ret_gtid, mst_log, mst_pos, exe_gtid, **kwargs):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = gtid_mode
        self.retrieved_gtid = ret_gtid
        self.mst_log = mst_log
        self.mst_read_pos = mst_pos
        self.exe_gtid = exe_gtid
        self.relay_mst_log = kwargs.get("relay_log")
        self.exec_mst_pos = kwargs.get("exe_pos")


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_sql_not_synced_non_gtid
        test_sql_synced_non_gtid
        test_sql_not_synced_gtid
        test_sql_synced_gtid

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

    def test_sql_not_synced_non_gtid(self):

        """Function:  test_sql_not_synced_non_gtid

        Description:  Test with SQL is not synced with non-GTID.

        Arguments:

        """

        master = MasterRep(None, None, "File1", 12345)
        slave = SlaveRep(None, None, None, None, None, relay_log="File1",
                         exe_pos=12346)

        self.assertTrue(mysql_libs.sql_rep_chk(master, slave))

    def test_sql_synced_non_gtid(self):

        """Function:  test_sql_synced_non_gtid

        Description:  Test with SQL is synced with non-GTID.

        Arguments:

        """

        master = MasterRep(None, None, "File1", 12345)
        slave = SlaveRep(None, None, None, None, None, relay_log="File1",
                         exe_pos=12345)

        self.assertFalse(mysql_libs.sql_rep_chk(master, slave))

    def test_sql_not_synced_gtid(self):

        """Function:  test_sql_not_synced_gtid

        Description:  Test with SQL is not synced with GTID.

        Arguments:

        """

        master = MasterRep("Yes", 12345, None, None)
        slave = SlaveRep("Yes", None, None, None, 12346, relay_log=None,
                         exe_pos=None)

        self.assertTrue(mysql_libs.sql_rep_chk(master, slave))

    def test_sql_synced_gtid(self):

        """Function:  test_sql_synced_gtid

        Description:  Test with SQL is synced with GTID.

        Arguments:

        """

        master = MasterRep("Yes", 12345, None, None)
        slave = SlaveRep("Yes", None, None, None, 12345, relay_log=None,
                         exe_pos=None)

        self.assertFalse(mysql_libs.sql_rep_chk(master, slave))


if __name__ == "__main__":
    unittest.main()
