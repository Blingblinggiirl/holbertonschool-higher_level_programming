#!/usr/bin/python3
for i in range(0, 100):
    if (i % 10 != i / 10): #if last digit is diferent to the first
        if (i % 10 <= i / 10): #if last digit is menor to the first
            continue
        if (i % 10 == i / 10):
            continue
        else:
            print("{:02d}".format(i), end=', ')
