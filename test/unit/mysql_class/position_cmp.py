# Classification (U)

"""Program:  position_cmp.py

    Description:  Unit testing of Position.cmp in mysql_class.py.

    Usage:
        test/unit/mysql_class/position_cmp.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_file_after2
        test_file_after
        test_file_before2
        test_file_before
        test_pos_after
        test_pos_before
        test_file_pos_equal

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        fname = "mysql-bin.00001"
        fname2 = "mysql-bin.00002"
        fname3 = "mysql-bin.00003"
        pos = 101
        pos2 = 102
        pos3 = 103

        self.master = mysql_class.Position(fname2, pos2)
        self.slave1 = mysql_class.Position(fname2, pos)
        self.slave2 = mysql_class.Position(fname2, pos2)
        self.slave3 = mysql_class.Position(fname2, pos3)
        self.slave4 = mysql_class.Position(fname, pos)
        self.slave5 = mysql_class.Position(fname3, pos3)
        self.slave6 = mysql_class.Position(fname3, pos2)
        self.slave7 = mysql_class.Position(fname, pos2)

    def test_file_after2(self):

        """Function:  test_file_after2

        Description:  Test with file after other file.

        Arguments:

        """

        self.assertEqual(self.master.cmp(self.slave6), -1)

    def test_file_after(self):

        """Function:  test_file_after

        Description:  Test with file after other file.

        Arguments:

        """

        self.assertEqual(self.master.cmp(self.slave5), -1)

    def test_file_before2(self):

        """Function:  test_file_before2

        Description:  Test with file before other file.

        Arguments:

        """

        self.assertEqual(self.master.cmp(self.slave7), 1)

    def test_file_before(self):

        """Function:  test_file_before

        Description:  Test with file before other file.

        Arguments:

        """

        self.assertEqual(self.master.cmp(self.slave4), 1)

    def test_pos_after(self):

        """Function:  test_pos_after

        Description:  Test with position after other position.

        Arguments:

        """

        self.assertEqual(self.master.cmp(self.slave3), -1)

    def test_pos_before(self):

        """Function:  test_pos_before

        Description:  Test with position before other position.

        Arguments:

        """

        self.assertEqual(self.master.cmp(self.slave1), 1)

    def test_file_pos_equal(self):

        """Function:  test_positions_equal

        Description:  Test with positions equal.

        Arguments:

        """

        self.assertEqual(self.master.cmp(self.slave2), 0)


if __name__ == "__main__":
    unittest.main()
