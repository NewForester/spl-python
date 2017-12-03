"""
    Python 3 solution to the Exercism exercise 'kindergarten garden'
"""

class Garden(object):
    """
    a class to hold state between calls to the only public method
    """
    _plants = ("Clover", "Grass", "Radishes", "Violets")
    _class = ("Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry")

    def __init__(self, diagram, students=None):
        """
        initialise internal state from parameters and/or defaults
        """
        self._diagram = diagram.split()
        self._students = sorted(students) if students else Garden._class
        self._plants = self._plants_by_initial(Garden._plants)

    @staticmethod
    def _plants_by_initial(plants):
        """
        return lookup-by-initial-letter dictionary of plant names
        """
        return dict(zip([p[0] for p in plants], plants))

    def rank(self, student):
        """
        return the cardinal rank of a student's plants on the window sills
        """
        return self._students.index(student)

    def _initials(self, rank):
        """
        return the initials of a student's plants given their cardinal rank
        """
        return [self._diagram[row][offset]
                for row in [0, 1] for offset in [2 * rank, 2 * rank + 1]]

    def plants(self, student):
        """
        return the names of the plants looked after by the named student
        """
        return [self._plants[ii] for ii in self._initials(self.rank(student))]

##
## A simple exercise that I can see other students not taking seriously.
##
## This was an exercise in one comment, one idea; one idea one line of code.
##
## Also the first time I have used a list comprehension over two loops.
## And first time I have used a zip too.
##
## Other solutions ? Two passes out of ten.  Two solutions did it all in
## __init__() and six did it all in plants().  One did everything in one line,
## at least one used a double comprehension and at least one used a zip (but
## for a different purpose).
##
## OOPS - self._plants is the same as Garden._plants &c &c
##
