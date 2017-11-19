"""
    Python 3 solution to the Exercism 'sieve' exercise
"""
def sieve(limit):
    """
    return list of primes up to limit using the Sieve of Eratosthenes
    """
    if limit < 2:
        return []

    candidates = list(range(limit + 1))
    candidates[0] = None
    candidates[1] = None

    prime = 2
    while prime * prime <= limit:
        if candidates[prime] != None:
            multiple = prime + prime
            while multiple <= limit:
                candidates[multiple] = None
                multiple += prime

        prime = prime + 1

    return [candidate for candidate in candidates if not candidate is None]

##
## This second iteration has no clever filtering of a list of potential primes.
## It has just one list that is filtered at the very end.
##
## Cutting out the list overhead will probably speed up the algorithm in any
## language.  It has been claimed it may speed it up by an order of magnitude.
##
