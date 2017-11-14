"""
    Python 3 solution to the Exercism 'pangram' exercise
"""
def is_pangram(sentence):
    """
    return true if 'sentence' is an pangram
    """
    sentence = sentence.lower()

    return all(sentence.find(c) != -1 for c in 'abcdefghijklmnopqrstuvwxyz')

##
## Pylint complained about my use of map + lambda.
## Apparently deprecated in favour of list comprehensions
## but generator expressions, as here, are to be preferred.
##
