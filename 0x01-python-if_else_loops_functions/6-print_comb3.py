#!/usr/bin/python3
for i in range(9):
    for j in range(1+i, 10):
        if (i == 8):
            print("{}{}".format(i, j))
        print("{}{}, ".format(i, j), end = "")
