#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = repr(number)
last_digit_string = number_string[-1]
last_digit_int = int(last_digit_string)
print(f"The last digit of {number} is {last_digit_int}")
