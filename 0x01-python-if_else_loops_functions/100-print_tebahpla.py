#!/usr/bin/python3
for i in range(122, 64, -1):
    print(f"{chr(i)}", end='')
    if i >= 97:
        i -= 25
