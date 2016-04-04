#!/usr/bin/python3
"""
an example of recursive programming

Provides a script/function to calculate terms of the Fibonacci series.

This example of the power of recursion has log(n) time complexity.
It takes advantage of the identities:

    F(2n-1) = F(n) * F(n) + F(n-1) * F(n-1)
    F(2n) = (2 * F(n-1) + F(n)) * F(n)

Deriving higher order terms by multiplication of lower order terms
instead of by addition implies better than linear performance.

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

    odd = nth % 2

    if nth == 1:
        acc = (0, 1)
    elif odd:
        acc = _internal((nth - 1) / 2)
    else:
        acc = _internal(nth / 2)

    acc = acc[0]*(acc[0]+2*acc[1]), acc[0]*acc[0]+acc[1]*acc[1]

    if odd:
        acc = acc[0]+acc[1], acc[0]

    return acc

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
