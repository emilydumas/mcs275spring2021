"""Classes representing robots in a simulation"""
# MCS 275 Spring 2021 David Dumas
# Lectures 5 and 6

from plane import Point,Vector
import random

class Bot:
    """Base class for all robots.  Sits in one place forever."""
    def __init__(self,position):
        """Setup with initial position `position`"""
        self.alive = True
        self.position = position # intended to be a plane.Point instance
    
    def __str__(self):
        """Human-readable string representation"""
        return "{}(position={},alive={})".format(
            self.__class__.__name__,
            self.position,
            self.alive
        )

        # self.__class__ is Bot
        # self.__class__.__name__ is "Bot"

    def __repr__(self):
        """Unambiguous string representation"""
        return str(self)

    def update(self):
        """Advance one time step (by doing nothing)"""

class WanderBot(Bot):
    """Robot that wanders randomly"""
    steps = [ Vector(1,0),
              Vector(0,1),
              Vector(-1,0),
              Vector(0,-1) ]  # Class attribute
    def __init__(self,position):
        """Setup wandering robot with initial position `position`"""
        # Call the constructor of Bot
        super().__init__(position)
        # WanderBot-specific initialization
    
    def update(self):
        """Take one random step"""
        self.position += random.choice(self.steps)
        #             ^ ends up calling Point.__add__(Vector)

class DestructBot(Bot):
    """Robot that sits in one place for a while, then self-destructs"""
    def __init__(self,position,lifetime):
        """Setup a bot at position `position` that sits for
        `lifetime` steps before self-destructing."""
        super().__init__(position)
        self.lifetime = lifetime # number of steps remaining

    def update(self):
        """Decrease lifetime by one unit, and self-destruct
        if it reaches zero."""
        # We only decrease the lifetime if it is
        # nonzero.  That way, once it reaches zero,
        # it stays there.
        if self.lifetime:
            self.lifetime -= 1

        # alive should be True if lifetime>0,
        # or False if lifetime==0.
        self.alive = bool(self.lifetime)

class PatrolBot(Bot):
    """Robot that walks back and forth along a fixed route"""
    def __init__(self,position,direction,nstep):
        """Setup a bot at position `position` that takes steps
        along the vector `direction` for `nstep` units of time
        before turning around and going back.  This cycle
        repeats forever."""
        super().__init__(position)
        self.direction = direction
        self.nstep = nstep # total length of patrol route (number of steps)
        self.count = self.nstep # steps left before the next turn

    def update(self):
        """Take one step, turn around if appropriate"""
        self.position += self.direction # take one step
        self.count -= 1
        if self.count == 0:
            self.direction = -1*self.direction # turn around
            self.count = self.nstep
        
# TODO: Add __str__ methods in the other Bots that report
# their vital stats, like lifetime, direction, etc.
# (The inherited __str__ from Bot only shows position & alive)        
        
    
