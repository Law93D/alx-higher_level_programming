#!/usr/bin/python3
def uppercase(str):
    for char in str:
        temp = char
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(char) - 32)
        print("{}".format(temp), end='')
    print()
