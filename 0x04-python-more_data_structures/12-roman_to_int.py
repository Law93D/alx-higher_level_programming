#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    old_num = 0

    for char in roman_string[::-1]:
        new_num = roman_numerals[char]
        if new_num >= old_num:
            result += new_num
        else:
            result -= new_num
        old_num = new_num

    return result
