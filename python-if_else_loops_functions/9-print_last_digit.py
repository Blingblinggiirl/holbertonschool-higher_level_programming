#!/urs/bin/python3
def print_last_digit(number):
    for number in range(0, ):
        if number < 0:
            number = -(-number % 10)
        else:
            number = number % 10
        print("{}".format(number), end="")
        return number
