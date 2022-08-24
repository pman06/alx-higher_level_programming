#!/usr/bin/python3
def uppercase(str):
    for val in str:
        if ord(val) >= ord('a') and ord(val) <= ord('z'):
            c = chr(ord(val) - 32)
        else:
            c = val
        print("{}".format(c), end="")
    print("")
