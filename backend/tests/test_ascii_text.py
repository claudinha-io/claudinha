from claudinha_text.ascii_converter import map_letter, message, step
from bitarray import bitarray

def test_map_letter_A():
    assert map_letter('A') == [
        bitarray('00000000'),
        bitarray('00111100'),
        bitarray('00100100'),
        bitarray('00111100'),
        bitarray('00100100'),
        bitarray('00100100'),
        bitarray('00100100'),
        bitarray('00000000')
    ]


def test_map_number_5():
    assert map_letter('5') == [bitarray('00000000'), bitarray('00111100'), bitarray('00100000'), bitarray('00011100'), bitarray('00000100'), bitarray('00000100'), bitarray('00111100'), bitarray('00000000')]


def test_word_without_number_and_lowcase_in_message():
    assert message("Palavra") == [[bitarray('00000000'), bitarray('00000000'), bitarray('00000000'), bitarray('00000000'), bitarray('00000000'), bitarray('00000000'), bitarray('00000000'), bitarray('00000000')], [bitarray('00000000'), bitarray('00111100'), bitarray('00100100'), bitarray('00111100'), bitarray('00100000'), bitarray('00100000'), bitarray('00100000'), bitarray('00000000')], [bitarray('00000000'), bitarray('00111100'), bitarray('00100100'), bitarray('00111100'), bitarray('00100100'), bitarray('00100100'), bitarray('00100100'), bitarray('00000000')], [bitarray('00000000'), bitarray('00100000'), bitarray('00100000'), bitarray('00100000'), bitarray('00100000'), bitarray('00100000'), bitarray('00111100'), bitarray('00000000')], [bitarray('00000000'), bitarray('00111100'), bitarray('00100100'), bitarray('00111100'), bitarray('00100100'), bitarray('00100100'), bitarray('00100100'), bitarray('00000000')], [bitarray('00000000'), bitarray('00100100'), bitarray('00100100'), bitarray('00100100'), bitarray('00100100'), bitarray('00100100'), bitarray('00011000'), bitarray('00000000')], [bitarray('00000000'), bitarray('00111100'), bitarray('00100100'), bitarray('00111100'), bitarray('00110000'), bitarray('00101000'), bitarray('00100100'), bitarray('00000000')], [bitarray('00000000'), bitarray('00111100'), bitarray('00100100'), bitarray('00111100'), bitarray('00100100'), bitarray('00100100'), bitarray('00100100'), bitarray('00000000')]]


def test_word_without_number_and_lowcase_in_step():
    word = message("Palavra:")
    assert step(word) == [bitarray('000000000000000000000000000000000000000000000000000000000000000000000000'), bitarray('000000000011110000111100001000000011110000100100001111000011110000000000'), bitarray('000000000010010000100100001000000010010000100100001001000010010000011000'), bitarray('000000000011110000111100001000000011110000100100001111000011110000011000'), bitarray('000000000010000000100100001000000010010000100100001100000010010000000000'), bitarray('000000000010000000100100001000000010010000100100001010000010010000011000'), bitarray('000000000010000000100100001111000010010000011000001001000010010000011000'), bitarray('000000000000000000000000000000000000000000000000000000000000000000000000')]
