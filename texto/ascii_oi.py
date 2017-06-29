#!/usr/bin/env python

from time import sleep
from bitarray import bitarray

import unicornhat as unicorn

from ascii_alphabet import *

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(270)
invert = [7, 6, 5, 4, 3, 2, 1, 0]
unicorn.brightness(0.5)
width, height = unicorn.get_shape()


def message(text):
    display_message = []
    phrase = '  ' + text
    skip = 0
    for letter in (range(len(phrase))):
        if skip != 0:
            skip -= 1
        else:
            display_message.append(map_letter(phrase[letter].upper()))
    return(display_message)


def map_letter(letter):
    print(letter)
    if letter in mapping:
        return mapping[letter]
    else:
        return mapping['_']


def show(word):
    for w in range(8):
        for h in range(8):
            if word[w][h]:
                unicorn.set_pixel(w, invert[h], 200, 0, 255)
            else:
                unicorn.set_pixel(w, invert[h], 0, 0, 0)
    unicorn.show()


def step(input_text):
    phrase = [bitarray(''), bitarray(''), bitarray(''), bitarray(''), bitarray(''), bitarray(''), bitarray(''), bitarray('')]
    for w in range(len(input_text)):
        for i in range(len(input_text[w])):
            phrase[i] = phrase[i] + input_text[w][i]

    for s in range(len(phrase[0])):
        show(phrase)
        sleep(0.1)
        for i in range(8):
            phrase[i].pop(0)
            phrase[i].append(0)


for x in range(0, 10):
    step(message('Lobinha XD'))
    sleep(0.1)
