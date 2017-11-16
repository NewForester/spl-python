"""
    Python 3 solution to the Exercism 'sieve' exercise
"""
def sieve(limit):
    """
    return list of primes up to limit using the Sieve of Eratosthenes
    """
    def sieve_generator(limit):
        """
        generate primes up to limit using the Sieve of Eratosthenes
        """
        candidates = list(range(2, limit + 1))

        while candidates != []:
            prime = candidates[0]
            candidates = list(filter(lambda C: C % prime != 0, candidates[1:]))
            yield prime

    return list(sieve_generator(limit))

##
## No solution was as neat as mine.  All involved a double loop.
##
## Comments on his own work by mileskrains leads me to believe that
## filtering on one list at the end instead of each iteration might
## be faster if less clear.  I'm going write a second iteration.
##
