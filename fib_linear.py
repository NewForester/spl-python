#!/usr/bin/python3
"""
an example of recursive programming

Provides a script/function to calculate terms of the Fibonacci series.

This example of the power of recursion has linear time complexity.
During the calculation of F(n), F(n-1), ... F(0) are each calculated only once.

This is not an example of tail recursion but it was inspired by the idea.

"""

__author__ = """New Forester <NewForester@users.noreply.github.com>
MIT Licence @ https://opensource.org/licenses/MIT"""

import sys

# ------------------------------

def _internal (nth):
    """
    Internal calculation of the nth term of the Fibonacci series

    Parameters - nth (integer) - the term to calculate

    Return - (integer, integer) - the nth and nth-1 terms
    """
    if nth == 1:
        acc = (0, 1)
    else:
        acc = _internal(nth - 1)

    return (acc[0]+acc[1], acc[0])

def fibonacci (nth):
    """
    Calculate the nth term of the Fibonacci series

    Parameters - nth (integer) - the term to calculate

    Return - (integer) - the nth term
    """
    if nth >= 1:
        return _internal(nth)[0]
    else:
        return 0

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
