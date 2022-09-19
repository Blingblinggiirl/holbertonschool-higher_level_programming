#!/usr/bin/python3
def best_score(dic):
    score = 0
    posible_key = None
    if dic != None:
        for key, value in dic.items():
            if value > score:
                posible_key = key
                score = value
    return posible_key
