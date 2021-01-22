"""Points and vectors in the plane"""
# MCS 275 Spring 2021 David Dumas
# Lectures 4 and 5

# This version of the plane module includes additional features
# added between Lecture 4 and Lecture 5.

# The earlier version of this module that was created in the live
# coding part of Lecture 4 can be found at:
# https://github.com/daviddumas/mcs275spring2021/blob/ba4a305212a7a15a4c068368e14f74a58c81c76f/samplecode/plane.py

class Point:
    """A point in the plane"""
    def __init__(self,x,y):
        """Create a new point with coordinates x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Human-readable string representation of a Point"""
        return "Point({},{})".format(self.x,self.y)

    def __repr__(self):
        """String representation of a Point"""
        return str(self)

    def __sub__(self,other):
        """Point-Point gives displacement vector"""
        if isinstance(other,Point):
            return Vector(self.x-other.x,self.y-other.y)
        else:
            return NotImplemented

    def __eq__(self,other):
        """Point equality means coordinate equality"""
        if isinstance(other,Point):
            return self.x==other.x and self.y==other.y
        else:
            return False

class Vector:
    """A 2-dimensional vector"""
    def __init__(self,x=0.0,y=0.0):
        """Create a new vector with components x,y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Human-readable string representation of a Vector"""
        return "Vector({},{})".format(self.x,self.y)

    def __repr__(self):
        """String representation of a Vector"""
        return str(self)

    def __add__(self,other):
        """Vector-vector or Vector-Point addition"""
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y)
        elif isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        else:
            return NotImplemented

    def __radd__(self,other):
        """Point-Vector addition"""
        if isinstance(other,Point):
            return Point(self.x+other.x,self.y+other.y)
        else:
            return NotImplemented

    def __sub__(self,other):
        """Vector subtraction"""
        if isinstance(other,Vector):
            return Vector(self.x-other.x,self.y-other.y)
        else:
            return NotImplemented

    def __mul__(self,other):
        """Scalar multiplication (with Vector on the left)"""
        if isinstance(other, (int,float)):
            return Vector(self.x*other,self.y*other)
        else:
            return NotImplemented

    def __rmul__(self,other):
        """Scalar multiplication (with Vector on the right)"""
        return self*other

    def __abs__(self):
        """Norm of the vector"""
        return (self.x**2 + self.y**2)**0.5

    def __eq__(self,other):
        """Vector equality means component equality"""
        if isinstance(other,Vector):
            return self.x==other.x and self.y==other.y
        else:
            return False