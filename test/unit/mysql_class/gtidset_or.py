# Classification (U)

"""Program:  gtidset_or.py

    Description:  Unit testing of GTIDSet.__or__ method in mysql_class.py.

    Usage:
        test/unit/mysql_class/gtidset_or.py

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
        test_or_not_subset
        test_or_subset

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gtidset1 = "50ceee08-9500-11ea-b699-002170204789:1-43"
        self.gtidset2 = "50ceee08-9500-11ea-b699-002170204789:43-43"
        self.gtidset3 = "50ceee08-9500-11ea-b699-002170204789:1-41"
        self.gtidset4 = "50ceee08-9500-11ea-b699-002170204789:1-41:43-43"

    def test_or_not_subset(self):

        """Function:  test_or_not_subset

        Description:  Test set 1 is not subset of set 2.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset3)
        gtid2 = mysql_class.GTIDSet(self.gtidset2)
        results = mysql_class.GTIDSet(self.gtidset4)
        data = gtid1 | gtid2

        self.assertEqual(data.gtids, results.gtids)

    def test_or_subset(self):

        """Function:  test_or_subset

        Description:  Test set 1 is subset of set 2.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid2 = mysql_class.GTIDSet(self.gtidset2)
        data = gtid1 | gtid2

        self.assertEqual(data.gtids, gtid1.gtids)


if __name__ == "__main__":
    unittest.main()
