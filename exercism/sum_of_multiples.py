"""
    Python 3 solution to the Exercism 'sum of multiples' exercise
"""
def sum_of_multiples(limit, numbers):
    """
    return the sum of multiples, up to limit, of any divisors from numbers
    """
    return sum(x for x in range (1, limit) if any(x % n == 0 for n in numbers))

##
## Translated from my erlang solution.
## Note is inner and outer loops are inverted wrt the read me description.
##
## Two of ten other solutions inverted the loops; one looked a lot like mine.
## The eight all used set to remove duplicates before summing.
##
## Sorting numbers into ascending order might improve things.
##
