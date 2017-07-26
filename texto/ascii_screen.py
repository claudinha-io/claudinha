#!/usr/bin/env python

import unicornhat as unicorn
from time import sleep
from itertools import product

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(270)
unicorn.brightness(0.5)
width, height = unicorn.get_shape()

invert = [7, 6, 5, 4, 3, 2, 1, 0]

colors = {}
colors['white'] = (255, 255, 255)     # #FFFFFF
colors['red'] = (255, 0, 0)           # #FF0000
colors['green'] = (0, 255, 0)         # #00FF00
colors['blue'] = (0, 0, 255)          # #0000FF
colors['yellow'] = (255, 255, 0)      # #FFFF00
colors['cyan'] = (0, 255, 255)        # #00FFFF
colors['magenta'] = (255, 0, 255)    # #FF00FF


def show(word, color):
    rgb = []
    if color in colors:
        rgb = colors[color]
    else:
        rgb = colors['white']
    for w, h in product(range(width), range(height)):
        if word[w][h]:
            unicorn.set_pixel(w, invert[h], rgb[0], rgb[1], rgb[2])
        else:
            unicorn.set_pixel(w, invert[h], 0, 0, 0)
    unicorn.show()


def show_display(phrase, color='white'):
    for s in range(len(phrase[0])):
        show(phrase, color)
        sleep(0.1)
        for i in range(8):
            phrase[i].pop(0)
            phrase[i].append(0)
