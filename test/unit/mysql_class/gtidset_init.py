# Classification (U)

"""Program:  gtidset_init.py

    Description:  Unit testing of GTIDSet.__init__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/gtidset_init.py

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
import mysql_class                          # pylint:disable=E0401,C0413
import version                              # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_gtidset_basestring
        test_gtidset_init

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gtidset = "35588520:333217-740055"
        self.results = {"35588520": [(333217, 740055)]}

    @mock.patch("mysql_class.isinstance", mock.Mock(return_value=False))
    def test_gtidset_basestring(self):

        """Function:  test_gtidset_basestring

        Description:  Test with basestring parameter.

        Arguments:

        """

        gtid = mysql_class.GTIDSet(self.gtidset)

        self.assertEqual(gtid.gtids, self.results)

    def test_gtidset_init(self):

        """Function:  test_gtidset_init

        Description:  Test GTIDSet.__init__ method.

        Arguments:

        """

        gtid = mysql_class.GTIDSet(self.gtidset)

        self.assertEqual(gtid.gtids, self.results)


if __name__ == "__main__":
    unittest.main()
