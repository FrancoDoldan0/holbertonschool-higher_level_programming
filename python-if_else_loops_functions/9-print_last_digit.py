#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    num1 = number % 10
    print(num1, end="")
    return num1
