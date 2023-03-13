#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_length = len(sentence)
    if sentence[0] is None:
        first_char = None
    else:
        first_char = sentence[0]
    return tuple_length, first_char
