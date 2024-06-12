"""Robot motion simulation with simple text-based graphics"""
# MCS 275 Spring 2021 - Emily Dumas
# Used in Lecture 5 and Lecture 6

from plane import Vector,Point
import bots
import random
import time

width=60
height=30

current_bots = []

# Make some wander bots
for i in range(5):
    P = Point(random.randint(0,width-1),random.randint(0,height-1))
    current_bots.append(bots.WanderBot(position=P))

# Make some patrol bots
patrol_directions = [ 
    Vector(1,0),
    Vector(0,1),
    Vector(1,1)
]
for i in range(10):
    P = Point(random.randint(0,width-1),random.randint(0,height-1))
    D = random.choice(patrol_directions)
    current_bots.append(bots.PatrolBot(position=P,direction=D,nstep=8))

# Make two destruct bots
current_bots.append(bots.DestructBot(position=Point(4,4),lifetime=5))
current_bots.append(bots.DestructBot(position=Point(4,10),lifetime=15))

# Symbols for the different kinds of bots
botsymbols = {
    bots.PatrolBot: "P",
    bots.DestructBot: "D",
    bots.WanderBot: "W",
    bots.Bot: "*"
}

print("Press ENTER to begin the simulation")
input()

n=0
while True:
    print("\n"*2*height)
    board = [ [" "]*width for _ in range(height) ]
    for b in current_bots:
        if not b.alive:
            continue
        elif b.position.x < 0 or b.position.x >= width:
            continue
        elif b.position.y < 0 or b.position.y >= height:
            continue
        # Mark the spot with a symbol depending on bot type
        board[b.position.y][b.position.x] = botsymbols[b.__class__]
    
    # To print the board, we'll print a lot of newlines, then
    # the board itself, and then the time indicator.  We'll put those
    # into a single string to reduce the chance that part of the display
    # is updated before the whole thing is shown.  This makes the
    # "graphics" a little more fluid.
    boardstr = "\n"*3*height
    for row in board:
        boardstr+="".join(row) + "\n"
    boardstr += "time={}".format(n)
    print(boardstr,flush=True)
    time.sleep(0.2)

    for b in current_bots:
        b.update()
    n += 1
