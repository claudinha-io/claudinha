#!/usr/bin/env python

from bitarray import bitarray
from itertools import product
import sys

from ascii_alphabet import *
from ascii_screen import *


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
    if letter in mapping:
        return mapping[letter]
    else:
        return mapping['_']


def step(input_text):
    phrase = [bitarray(''), bitarray(''), bitarray(''), bitarray(''),
              bitarray(''), bitarray(''), bitarray(''), bitarray('')]
    for w, i in product(range(len(input_text)), range(8)):
        phrase[i] = phrase[i] + input_text[w][i]
    return phrase


for x in range(0, 2):
    text = step(message('Teste'))
    if len(sys.argv) == 2:
        show_display(text, sys.argv[1])
    else:
        show_display(text)
