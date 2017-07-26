#!/usr/bin/env python

from bitarray import bitarray
from itertools import product
import sys

from ascii_alphabet import mapping
from ascii_screen import show_display


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


if __name__ == '__main__':
    text = []
    if len(sys.argv) == 2:
        text = step(message(sys.argv[1]))
        show_display(text)
    if len(sys.argv) > 2:
        text = step(message(" ".join(sys.argv[2:])))
        show_display(text, sys.argv[1])
    else:
        show_display(step(message('Teste')))
