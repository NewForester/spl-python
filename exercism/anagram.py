"""
    Python 3 solution to the Exercism 'anagram' exercise
"""
from collections import Counter

def detect_anagrams(word, candidates):
    """
    return the list (grr) of candidates that are anagrams of word
    """
    lower = word.lower()
    counts = Counter(lower)

    def yield_anagram():
        """
        return the anagrams of word one by one
        """
        for candidate in candidates:
            lower_candidate = candidate.lower()
            if Counter(lower_candidate) == counts:
                if lower_candidate != lower:
                    yield candidate

    return list(yield_anagram())

##
## This iteration uses Counter instead of sorted() but the real interest here
## is the attempt to use a generator.  Sadly the test cases are a tad dumb.
##
