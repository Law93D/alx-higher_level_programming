#!/usr/bin/python3
def fizzbuzz():
    for char in range(1, 101):
        if char % 3 == 0 and char % 5 != 0:
            print("Fizz ", end='')
        elif char % 5 == 0 and char % 3 != 0:
            print("Buzz ", end='')
        elif char % 5 == 0 and char % 3 == 0:
            print("Fizzbuzz ", end='')
        else:
            print("{} ".format(char), end='')
