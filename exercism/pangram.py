"""
    Python 3 solution to the Exercism 'pangram' exercise
"""
def is_pangram(sentence):
    """
    return true if 'sentence' is an pangram
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    sentence = sentence.lower()

    return all(map(lambda c: sentence.find(c) != -1, alpha))

##
## No other solution I examined used two higher level functions or a lambda.
##
