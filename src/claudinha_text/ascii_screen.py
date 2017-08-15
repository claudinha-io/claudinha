#!/usr/bin/env python

import unicornhat as unicorn
from time import sleep
from itertools import product as matriz

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
    """
    Exibe os pixels nas posições corretas no display do Unicorn Hat.

    Cria uma lista contendo os valores RGB da cor escolhida e aplica as \
    posições dos pixels determinadas na matriz bidirecional 'word' e por \
    fim exibe no display.

    Args:
        word (list[bitarray]): Frase em formato de bitarray
        color (string): Cor para exibição no display. Padrão: Branco

    """
    rgb = []
    if color in colors:
        rgb = colors[color]
    else:
        rgb = colors['white']
    for w, h in matriz(range(width), range(height)):
        if word[w][h]:
            unicorn.set_pixel(w, invert[h], rgb[0], rgb[1], rgb[2])
        else:
            unicorn.set_pixel(w, invert[h], 0, 0, 0)
    unicorn.show()


def show_display(phrase, color='white'):
    """
    Exibe a frase em scroll no display do Unicorn Hat.

    Executa um loop percorrendo todo o comprimento da matriz bidimensional \
    'phrase' pela altura do display. Dentro do loop chama o método show() \
    passando o objeto 'phrase' e a string color como parametro, para exibir \
    os pixels nas posições corretas no display. Depois elimina o conteudo da \
    primeira posição de cada linha da matriz e completa com 0 o final da \
    lista, mantendo o comprimento.

    Args:
        phrase (list[bitarray]): Frase em formato de bitarray
        color (string): Cor para exibição no display. Padrão: Branco

    """
    for i, collum_position in matriz(range(len(phrase[0])), range(height)):
        show(phrase, color)
        phrase[collum_position].pop(0)
        phrase[collum_position].append(0)
        sleep(0.01)

