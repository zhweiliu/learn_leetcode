from typing import Dict, List

'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace. Check if the next character (if not already at the end of the string) is 
'-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive 
respectively. Assume the result is positive if neither is present. Read in next the characters until the next 
non-digit charcter or the end of the input is reached. The rest of the string is ignored. Convert these digits into 
an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as 
necessary (from step 2). If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the 
integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, 
and integers greater than 231 - 1 should be clamped to 231 - 1. Return the integer as the final result. Note: 

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


'''


def myAtoi(s: str) -> int:
    max_digital = 2 ** 31 - 1
    min_digital = -2 ** 31
    is_scanned_digital = False
    is_scanned_sign = False
    accepted_ascii = ['-', '+'] + [str(i) for i in range(10)]
    keep_char = []
    for i in range(len(s)):
        c = s[i]
        # leading whitespace
        if c == ' ' and len(keep_char) == 0:
            continue

        if len(keep_char) == 0 and c not in accepted_ascii:
            return 0

        if c not in accepted_ascii:
            break

        if c in accepted_ascii[:2] and is_scanned_sign:
            break

        if c not in accepted_ascii and is_scanned_digital:
            break

        if c in accepted_ascii:
            keep_char.append(c)
            if c in accepted_ascii[:2]:
                is_scanned_sign = True
            if c in accepted_ascii[2:]:
                is_scanned_digital = True

    convert_digital = 0
    try:
        while keep_char[-1] in ['-', '+']:
            keep_char.pop(-1)

        convert_digital = int(float(''.join(keep_char)))

        if convert_digital > max_digital:
            convert_digital = max_digital

        if convert_digital < min_digital:
            convert_digital = min_digital
    except:
        pass
    finally:
        return convert_digital


if __name__ == '__main__':
    test_set = [
        '42',
        '   -42',
        '4193 with words',
        'words and 987',
        '-91283472332',
        '.1',
        '  -0012a42',
        "    +0a32",
        '-5-',
        "-13+8",
        '123-',
    ]
    answer_set = [
        42,
        -42,
        4193,
        0,
        -2147483648,
        0,
        -12,
        0,
        -5,
        -13,
        123
    ]
    for data in zip(test_set, answer_set):
        print(f'the string {data[0]} atoi is { "" if myAtoi(data[0]) == data[1] else "not " }passed')
