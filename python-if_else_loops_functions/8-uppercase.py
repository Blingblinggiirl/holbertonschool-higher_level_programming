#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letra = ord(i)
        if letra > 96 and letra < 123:
            letra = letra - 32
        print("{}".format(chr(letra)), end='')
        print('')
