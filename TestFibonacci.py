"""
    unit test for fib_*.py

Verifies the fibonacci() function returns the correct value for
the first 10 terms of the Fibonacci series.

By induction, the function works for all other positive integers.

The test is run for two implementations of fibonacci():
  - exponential complexity (dumb implementation)
  - linear complexity (inspired by functional programming)

"""

__author__ = """New Forester <NewForester@users.noreply.github.com>
MIT Licence @ https://opensource.org/licenses/MIT"""

import unittest

import fib_exponential as exponential
import fib_linear as linear

class TestHello (unittest.TestCase):
    """
    test class for fib_*.py
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

    def test_exponential_fibonacci (self):
        """
        The test case for fibonacci() in fib_exponential.py.
        """
        self._run_test("exponential fibonacci algorithm", exponential.fibonacci)

    def test_linear_fibonacci (self):
        """
        The test case for fibonacci() in fib_linear.py.
        """
        self._run_test("linear fibonacci algorithm", linear.fibonacci)

    def _run_test (self, msg, fibonacci):
        """
        Run a simple test of an implementation of the Fibonacci series.

        Verifies the function under test returns the correct result for the first 10 terms of the series.
        """
        print("\nTest {0} ...".format(msg))

        nn, mm = 1, 0

        for ii in range(1, 11):
            cardinal = ("th", "st", "nd", "rd")[ii if (ii < 4) else 0]

            self.assertEqual(fibonacci(ii), nn,
                '{0}{1} Fibonacci number'.format(ii, cardinal))

            nn, mm = nn+mm, nn

if __name__ == '__main__':
    unittest.main()

# EOF
