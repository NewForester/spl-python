"""
    Python 3 solution to the Exercism 'word count' exercise
"""
def word_count(phrase):
    """
    given a phrase, count the occurrences of each word in that phrase

    words comprise alphanumeric characters and are separated by anything else
    """
    counts = {}

    for word in ''.join(
            map(lambda c: c.lower() if c.isalnum() else ' ', phrase)).split():
        try:
            counts[word] = counts[word] + 1
        except KeyError:
            counts[word] = 1

    return counts

##
## There was greater variation in solutions, suggesting people found this
## exercise more difficult.  Not all used try/except and although all had
## to clean the input string, none did is as succinctly.
##
