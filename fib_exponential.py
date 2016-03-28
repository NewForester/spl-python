#!/usr/bin/python3
"""
an example of dumb recursive programming

Provides a script/function to calculate terms of the Fibonacci series.

This is a simple, elegant but deceptive example of the power of recursion.
During the calculation of F(n), F(1) is calculated not once, but F(n) times.

At a guess, the time complexity is exponential or O(c**n) where c is 1.6180...
(otherwise known as the golden ratio).

"""

__author__ = """New Forester <NewForester@users.noreply.github.com>
MIT Licence @ https://opensource.org/licenses/MIT"""

import sys

# ------------------------------

def fibonacci (nth):
    """
    Calculate the nth term of the Fibonacci series

    Parameters - nth (integer) - the term to calculate

    Return - (integer) - the nth term
    """
    if nth <= 2:
        return 1 if nth > 0 else 0
    else:
        return fibonacci(nth - 2) + fibonacci(nth - 1)

# ------------------------------

if __name__ == '__main__':

    if len(sys.argv) > 1:
        # Print the nth Fibonacci number calculated using recursion

        print(fibonacci(int(sys.argv[1])))
    else:
        # Print the first few Fibonacci numbers using a loop

        nn, mm = 1, 0

        while nn < 100:
            print(nn, end=" ")
            nn, mm = nn+mm, nn

        print(nn)
# EOF
