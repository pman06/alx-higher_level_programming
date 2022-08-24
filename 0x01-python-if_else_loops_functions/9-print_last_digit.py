#!/usr/bin/python3
def print_last_digit(number):
    str = int(repr(number)[-1])
    print("{:d}".format(str), end="")
    return(str)
