"""Simulate kids playing with toys from a toybox"""
# MCS 275 Spring 2021 Lecture 9
# Demonstrates use of the context manager protocol
# to ensure toys are always returned to the toybox

# Suggestion: The first time you look at this code,
# read it from bottom to top.

import threading
import time
import random

class ToyManager:
    """Class that manages a toybox that can be accessed
    by multiple threads.  Toys can be checked in and out,
    and checking out a toy when the box is empty raises an
    exception."""
    def __init__(self):
        """Create a new toybox"""
        # List of toys initially available
        self.available = ["12KG CUBE OF TUNGSTEN","BALL","SCOOTER"]
        # Lock that is held whenever the list of available toys
        # is being checked or changed
        self.lock = threading.Lock()
    def check_out(self):
        """Get one of the available toys.  If none is
        available, raise an exception."""
        with self.lock:
            if self.available:
                return self.available.pop()
            else:
                raise Exception("No Toy available")
    def check_in(self,toy):
        """Put a toy back in the box"""
        with self.lock:
            self.available.append(toy)

# Note: ToyManager doesn't do any checking of toys being 
# returned, 

class Toy:
    """Context manager that represents a toy removed
    from a specific toybox which is automatically returned
    when play is complete."""
    def __init__(self,manager):
        """Keep track of the toybox `manager` from which
        a toy will be removed."""
        self.manager = manager
    def __enter__(self):
        """Check out a toy (and remember which one we got)"""
        while True:
            try:
                self.toy = self.manager.check_out()
                return self.toy
            except Exception:
                # Nothing is available, so we wait
                # before trying again.
                print("Someone is waiting...")
                time.sleep(0.5)
    def __exit__(self,*args):
        """Return the toy that was checked out"""
        self.manager.check_in(self.toy)

class ToyUserThread(threading.Thread):
    """Simulation of a kid who alternates between relaxing
    and playing with toys"""
    def __init__(self,name,manager):
        """Create a named kid who is allowed to play with 
        toys from the toybox `manager`"""
        super().__init__(daemon=True)
        self.manager = manager
        self.name = name
    def run(self):
        """Simulate play"""
        while True:
            time.sleep(0.1)
            print("{} is relaxing".format(self.name),flush=True)
            time.sleep(0.5+random.random()*3)
            print("{} wants a toy".format(self.name),flush=True)
            with Toy(self.manager) as toy:
                print("{} starts playing with the {}".format(self.name,toy),flush=True)
                time.sleep(2+random.random()*4)
                print("{} returns the {}".format(self.name,toy),flush=True)

# --------------------------------------------------
# Main program begins here

# Create a toybox
M = ToyManager()
# Make simulated kids who know about the toybox
threadnames = [ "ALICE", "BOB", "CARLOS", "DAVID" ]
threads = [ ToyUserThread(n,M) for n in threadnames ]
# Start the kid simulation threads
[ T.start() for T in threads ]

# Main thread waits for Enter to be pressed
input()

# The kid threads are daemon threads, meaning they
# are terminated as soon as the main thread is done.
# Thus the program exits as soon as the user presses
# Enter.
