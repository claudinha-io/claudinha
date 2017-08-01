from bitarray import bitarray
from itertools import product

from claudinha_text.ascii_alphabet import mapping

height = 8

def message(text):
    display_message = []
    phrase = ' ' + text
    for letter in (range(len(phrase))):
        display_message.append(map_letter(phrase[letter].upper()))
    return(display_message)


def map_letter(letter):
    if letter in mapping:
        return mapping[letter]
    else:
        return mapping['_']


def step(input_text):
    phrase = height*[bitarray('')]
    for w, i in product(range(len(input_text)), range(height)):
        phrase[i] = phrase[i] + input_text[w][i]
    return phrase