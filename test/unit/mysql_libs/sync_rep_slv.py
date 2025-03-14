# Classification (U)

"""Program:  sync_rep_slv.py

    Description:  Unit testing of sync_rep_slv in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/sync_rep_slv.py

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
import mysql_libs                           # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class MasterRep():                          # pylint:disable=R0903

    """Class:  MasterRep

    Description:  Class stub holder for mysql_class.MasterRep class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.server_id = 10


class SlaveRep():                           # pylint:disable=R0903

    """Class:  SlaveRep

    Description:  Class stub holder for mysql_class.SlaveRep class.

    Methods:
        __init__

    """

    def __init__(self, mst_id=10, slv_stat=False):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.mst_id = mst_id
        self.slv_up = slv_stat

    def is_slv_running(self):

        """Method:  is_slv_running

        Description:  Stub holder for mysql_class.Server.is_slv_running method.

        Arguments:

        """

        return self.slv_up


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_logs_to_synced
        test_logs_not_synced
        test_logs_synced
        test_ids_not_match

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.master = MasterRep()

    @mock.patch("mysql_libs.sync_delay")
    @mock.patch("mysql_libs.is_logs_synced")
    def test_logs_not_synced(self, mock_sync, mock_delay):

        """Function:  test_logs_not_synced

        Description:  Test with logs are not synced.

        Arguments:

        """

        mock_delay.return_value = True
        mock_sync.side_effect = [False, True, False]
        slave = SlaveRep()
        err_msg = f"Error:  Server {slave} not in sync with master."

        self.assertEqual(mysql_libs.sync_rep_slv(self.master, slave),
                         (True, err_msg))

    @mock.patch("mysql_libs.sync_delay")
    @mock.patch("mysql_libs.is_logs_synced")
    def test_logs_to_synced(self, mock_sync, mock_delay):

        """Function:  test_logs_to_synced

        Description:  Test with logs are to be synced.

        Arguments:

        """

        mock_delay.return_value = True
        mock_sync.side_effect = [False, True, True]
        slave = SlaveRep()

        self.assertEqual(
            mysql_libs.sync_rep_slv(self.master, slave), (False, None))

    @mock.patch("mysql_libs.is_logs_synced")
    @mock.patch("mysql_libs.chg_slv_state")
    def test_logs_synced(self, mock_chg, mock_sync):

        """Function:  test_logs_synced

        Description:  Test with logs are synced.

        Arguments:

        """

        mock_chg.return_value = True
        mock_sync.return_value = True
        slave = SlaveRep(slv_stat=True)

        self.assertEqual(
            mysql_libs.sync_rep_slv(self.master, slave), (False, None))

    def test_ids_not_match(self):

        """Function:  test_ids_not_match

        Description:  Test Slave and Master IDs do not match.

        Arguments:

        """

        slave = SlaveRep(11)
        err_msg = \
            f"Error:  Slave's Master ID {slave.mst_id} doesn't" \
            f" match Master ID {self.master.server_id}."

        self.assertEqual(
            mysql_libs.sync_rep_slv(self.master, slave), (True, err_msg))


if __name__ == "__main__":
    unittest.main()
