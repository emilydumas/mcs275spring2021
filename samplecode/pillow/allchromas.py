"""Show all chromaticities in a bitmap image"""
# MCS 275 Spring 2021 Lecture 24
# Emily Dumas

from PIL import Image

img = Image.new("RGB",(256,256),color=(0,0,0))

for x in range(256):
    for y in range(256):
        r = x
        g = y
        b = 255 - x - y
        if b < 0:
            continue
        img.putpixel( (x,y), (r,g,b) )

img.save("chromaticities.png")
