"""
    Python 3 solution to the Exercism exercise 'acronym'
"""

def abbreviate(words):
    """
    return an acronym that represent 'words'
    """
    return(''.join([letter for (index, letter) in enumerate(words)
        if index == 0 or words[index-1] in [' ', '-']]).upper())

##
## My first use of enumerate:  avoid a loop counter used as an index.
##
## The more obvious solution is:
##
## return ''.join(w[0] for w in words.replace('-',' ').split()).upper()
##
## There were variations on this, include using re to do the split and
## a couple of unique but verbose solutions.
##
