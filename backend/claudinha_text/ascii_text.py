#!/usr/bin/env python3

import sys

from claudinha_text.ascii_screen import show_display
from claudinha_text.ascii_converter import step, message


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
