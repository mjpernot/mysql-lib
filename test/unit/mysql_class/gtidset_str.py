# Classification (U)

"""Program:  gtidset_str.py

    Description:  Unit testing of GTIDSet.__str__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/gtidset_str.py

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
        test_gtidset_str

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gtidset = "35588520:333217-740055"

    def test_gtidset_str(self):

        """Function:  test_gtidset_str

        Description:  Test GTIDSet.__str__ method.

        Arguments:

        """

        gtid = mysql_class.GTIDSet(self.gtidset)

        self.assertEqual(str(gtid), self.gtidset)


if __name__ == "__main__":
    unittest.main()
