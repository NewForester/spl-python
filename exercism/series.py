"""
    Python 3 solution to the Exercism 'series' exercise
"""
def slices(series, length):
    """
    return the 'set' of length n 'substrings'

    The tests cases require a list of lists of integers.
    """
    result = []

    if len(series) < length or length < 1:
        raise ValueError

    while len(series) >= length:
        result.append([int(x) for x in list(series[:length])])
        series = series[1:]

    return result

##
## Trivial exercises but the test cases are inconsistent with the read me.
##
