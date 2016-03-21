"""
    unit test for fibonacci.py

Verifies the fibonacci() function returns the correct value for
the first 10 terms of the Fibonacci series.

By induction, the function works for all other positive integers.

"""

__author__ = """New Forester <NewForester@users.noreply.github.com>
MIT Licence @ https://opensource.org/licenses/MIT"""

import unittest

from fibonacci import fibonacci

class TestHello (unittest.TestCase):
    """
    test class for fibonacci.py
    """
    def setUp (self):
        """
        Called before calling each test case routine.

        Performs any necessary pre-test set up.
        """
        pass    # print ("\nSet up")

    def tearDown (self):
        """
        Called after calling each test case routine.

        Performs any necessary post-test clean up and shut down.
        """
        pass    # print ("\nTear down")

    def test_fibonacci (self):
        """
        The test case for fibonacci() in fibonacci.py.

        Verifies the function for the first 10 terms of the Fibonacci series.
        """
        print("\n{0} ...".format("test fibonacci"))

        nn, mm = 1, 0

        for ii in range(1, 11):
            cardinal = ("th", "st", "nd", "rd")[ii if (ii < 4) else 0]

            self.assertEqual(fibonacci(ii), nn,
                '{0}{1} Fibonacci number'.format(ii, cardinal))

            nn, mm = nn+mm, nn

if __name__ == '__main__':
    unittest.main()

# EOF
