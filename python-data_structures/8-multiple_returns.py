#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return 0, None
    if sentence == "":
        return 0, None
    if sentence is not None:
        return len(sentence), sentence[0]
