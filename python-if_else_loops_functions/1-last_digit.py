#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    last_digit = number % 10
    print(f"Last digit of {number} is {last_digit} and is 0")
if number % 10 != 0:
    last_digit = -(-number % 10)
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
if number % 10 > 5:
    last_digit = number % 10
    print(f"Last digit of {number} is {last_digit} and is grater than 5")
elif number % 10 <= 5 and number % 10 != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")





#number_string = repr(number)
#last_digit_string = number_string[-1]
#last_digit_int = int(last_digit_string)
#if last_digit_int < 0:
 #   last_digit_int = int((last_digit_int % 10) * -1)
#if last_digit_int > 5:
 #   print(f"Last digit of {number} is {last_digit_int} and is grater than 5")
#if last_digit_int == 0:
 #   print(f"Last digit of {number} is {last_digit_int} and is 0")
#if last_digit_int < 6 and last_digit_int != 0:
 #   print(f"Last digit of {number} is {last_digit_int} and is less than 6 and not 0")

