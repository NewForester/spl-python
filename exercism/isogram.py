"""
    Python 3 solution to the Exercism 'isogram' exercise
"""
def is_isogram(string):
    """
    return true if 'string' is an isogram
    """
    string = string.lower()

    return not any(map(lambda c: c.isalpha() and string.count(c) != 1, string))

##
## No other solution I examined used two higher level functions or a lambda.
##
