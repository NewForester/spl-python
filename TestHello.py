"""
    unit test for hello.py

This is a simple unit test for hello.py written with a view to
  - checking that unittest is installed properly;
  - providing a simple starting point for writing other unit tests in python.

"""

__author__ = """New Forester <NewForester@users.noreply.github.com>
MIT Licence @ https://opensource.org/licenses/MIT"""

import unittest

from hello import greet

class TestHello (unittest.TestCase):
    """
    test class for hello.py
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

    def test_hello (self):
        """
        The test case for greet() in hello.py.

        Two simple tests.
        """
        print("\n{0} ...".format("test hello()"))

        self.assertEqual(greet('Paul'),    'Hello Paul',    'greeting failed')
        self.assertEqual(greet('Heather'), 'Hello Heather', 'greeting failed')

if __name__ == '__main__':
    unittest.main()

# EOF
