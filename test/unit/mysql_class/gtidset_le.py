# Classification (U)

"""Program:  gtidset_le.py

    Description:  Unit testing of GTIDSet.__le__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/gtidset_le.py

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
        test_gtidset_le_false
        test_gtidset_le_equal
        test_gtidset_le_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gtidset1 = "35588520:333217-740055"
        self.gtidset2 = "35588520:1-740055,76012896:1-502108"

    def test_gtidset_le_false(self):

        """Function:  test_gtidset_le_false

        Description:  Test GTIDSet.__le__ method for False return.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid2 = mysql_class.GTIDSet(self.gtidset2)

        self.assertGreater(gtid2, gtid1)

    def test_gtidset_le_equal(self):

        """Function:  test_gtidset_le_equal

        Description:  Test GTIDSet.__le__ for equal values.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid2 = mysql_class.GTIDSet(self.gtidset1)

        self.assertLessEqual(gtid1, gtid2)

    def test_gtidset_le_true(self):

        """Function:  test_gtidset_le_true

        Description:  Test GTIDSet.__le__ method for True return.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid2 = mysql_class.GTIDSet(self.gtidset2)

        self.assertLessEqual(gtid1, gtid2)


if __name__ == "__main__":
    unittest.main()
