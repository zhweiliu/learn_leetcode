from typing import List


def plusOne(digits: List[int]) -> List[int]:
    add_one = True
    based = 10
    for i in range(len(digits) - 1, -1, -1):
        num = digits[i] + 1 if add_one else digits[i]
        digits[i] = num % based
        add_one = True if int(num/based) > 0 else False
        if not add_one:
            break
    if add_one:
        digits.insert(0, 1)
    return digits


if __name__ == '__main__':
    digits = [9]

    # print(plusOne(digits))
    print(plusOne(digits))
