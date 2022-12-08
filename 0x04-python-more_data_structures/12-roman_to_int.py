#!/usr/bin/python3
def roman_to_int(roman_string):
    # Fail checks, none, not a string
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    # Dictionary for roman numerals
    r_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    temp = list(roman_string)
    # Concatenate 4 and 9s
    if len(temp) > 1:
        index = 0
        for i in temp:
            try:
                if temp[index] == 'I' and temp[index + 1] == 'V':
                    temp[index:index + 2] = [''.join(temp[index:index + 2])]
            except IndexError:
                pass
            try:
                if temp[index] == 'I' and temp[index + 1] == 'X':
                    temp[index:index + 2] = [''.join(temp[index:index + 2])]
            except IndexError:
                pass
            index += 1
    # Search in dictionary for correct numbers and add
    for k, v in r_dict.items():
        for index in temp:
            if index == k:
                result += v
    return result
