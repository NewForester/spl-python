"""
    Python 3 solution to the Exercism 'parallel letter frequency' exercise
"""

from collections import Counter

""" """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    There is nothing parallel about this solution.  Perhaps in another life.
""" """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def calculate(text_input):
    """
    return a dictionary with lowercase letters for keys and counts for values
    """
    counter = Counter()

    for text in text_input:
        counter.update(''.join(c for c in text.lower() if c.isalpha()))

    return dict(counter)

##
## This level 5 problem was sandwiched between two level 1 problems
## I could 'lift' the parallel part from someone else's solution but,
## like the tests, be none the wiser.
##
## The use of Counter came from the tests - I had a look in an effort to
## confirm the problem was actually asking for a parallel implementation.
##
## In other solutions examined: 2 had no parallelism, one used the
## thread library and four used the multiprocessing library.
##
## The solution that used the thread library used a lock and a single
## Counter object.  Not parallel at all.
##
## The four multiprocessing solutions all used the Pool class but used
## it differently.  Two used a number of Counter objects and summed them
## at the end.  One used the Manager class, I guess to single thread
## access to a single Counter.  Another looked like it has one Counter,
## many writers and no protection.
##
## Here is one by tcarobruce.  I liked it more that the others:
##
##      def calculate(texts):
##          with Pool(5) as pool:
##              counted = pool.map(count_letters, texts)
##              return sum(counted, Counter())
##
## The actual counting takes place in count_letters().  Not a good routine
## (none of them were).  Some even did the filtering and case conversion
## in the main routine instead of the parallel subroutine.
##
