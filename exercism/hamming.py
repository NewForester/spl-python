"""
    Python 3 solution to the Exercism 'hamming' exercise
"""
def distance(strand_a, strand_b):
    """
    return the hamming distance between two DNA strands of equal length

    make an effort to throw ValueError if strands are unequal in length
    """
    if len(strand_a) != len(strand_b):
        raise ValueError

    return sum(map(lambda a, b: a != b, strand_a, strand_b))

##
## Most solutions used a loop and do not look as neat
##
