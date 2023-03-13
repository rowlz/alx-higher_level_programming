#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] is None:
        first_char = None
        tuple_length = 0
        return tuple_length, first_char
    else:
        first_char = sentence[0]
        tuple_length = len(sentence)
        return tuple_length, first_char
