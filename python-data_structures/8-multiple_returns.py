#!/usr/bin/python3
def multiple_returns(sentence):
  lens = len(sentence)
  if lens != 0:
    return lens, sentnce[0]
  else:
    return lens, None
