"""Classes representing robots in a simulation"""
# MCS 275 Spring 2021 David Dumas
# Lecture 5

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
        return "{}(position={},alive={})".format(self.__class__.__name__,self.position,self.alive)

    def __repr__(self):
        """Unambiguous string representation"""
        return str(self)

    def update(self):
        """Advance one time step (by doing nothing)"""

class WanderBot(Bot):
    """Robot that wanders randomly"""
    def __init__(self,position):
        """Setup wandering robot with initial position `position`"""
        # Call the constructor of Bot
        super().__init__(position)
        # WanderBot-specific initialization
        self.steps = [ Vector(1,0),
                       Vector(0,1),
                       Vector(-1,0),
                       Vector(0,-1) ]
    
    def update(self):
        """Take one random step"""
        self.position += random.choice(self.steps)
        #             ^ ends up calling Point.__add__(Vector)