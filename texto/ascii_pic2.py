#!/usr/bin/env python

from time import sleep

import unicornhat as unicorn


print("""ASCII Pic

You should see a scrolling image, defined in the below variable ASCIIPIC.

If the smiley looks sad, change the rotation from 0 to 180.
""")

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

# Use exactly 8 lines to write your message
ASCIIPIC = [
     "XXX  XXX   X   XX      ", #1
     " X    X        XX      ", #2 
     " X    X   XX   XX      ", #3
     " XXXXXX    X   XX      ", #4
     " X    X    X   XX      ", #5
     " X    X    X           ", #6
     "XXX  XXX  XXX  XX      ", #7
     "                       ", #8
    ][::-1]
    
max_len = max(len(lin) for lin in ASCIIPIC)

pic = list(''.join(lin) for lin in zip(*ASCIIPIC))    
    
i = -1

def step():
    global i
    i = 0 if i>=100*len(pic) else i+1 # avoid overflow
    for h in range(height):
        for w in range(width):
            hPos = (i+h) % len(pic)
            chr = pic[hPos][w]
            if chr == ' ':
                unicorn.set_pixel(w, h, 0, 0, 0)
            else:
                unicorn.set_pixel(w, h, 255, 0, 0)
    unicorn.show()

while True:
    step()
    sleep(0.1)
