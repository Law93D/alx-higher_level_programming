#!/usr/bin/python3
import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("Number of argument(s): 0.")
    else:
        print(f"Number of argument(s): {num_arguments}:")

        for i in range(1, num_arguments + 1):
            print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    print_arguments()
