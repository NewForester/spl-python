"""
Python 3 solution to the Exercism 'robot simulator' exercise
"""

EAST    = 0
NORTH   = 1
WEST    = 2
SOUTH   = 3

class Robot(object):
    """
    simulate the movement of a robot on a Cartesian grid
    """
    def __init__(self, bearing=NORTH, x=0, y=0):
        self._cp = bearing
        self._x = x
        self._y = y

    @property
    def coordinates(self):
        """
        return the robot's current grid position
        """
        return self._x, self._y

    @property
    def bearing(self):
        """
        return the direction in which the robot is facing
        """
        return self._cp

    def turn_right(self):
        """
        turn the robot's bearing clockwise
        """
        self._cp -= 1
        self._cp %= 4

    def turn_left(self):
        """
        turn the robot's bearing anticlockwise
        """
        self._cp += 1
        self._cp %= 4

    def advance(self):
        """
        move the robot one grid position in the direction it is facing
        """
        self._x += (1,  0, -1,  0)[self._cp]
        self._y += (0,  1,  0, -1)[self._cp]

    def simulate(self, moves):
        """
        simulate robot movement as directed by a string of moves
        """
        [(self.advance, self.turn_right, self.turn_left)["ARL".index(move)]() for move in moves]

##
## No one saw fit to do an if ... elif solution.
##
## Those who used a plain list of cardinal points tended to use modulo
## arithmetic for the turn routines and did it the hard was for the
## advance routine.
##
## A few used tuples for the cardinal points that allow easy implementation
## of the advance routine but meant the turn routines had to be done the
## hard way.
##
## Some used dictionary.  No one used simple lookup or indexing.
##
## All used if .. elif and a for look in the simulate routine.
##
