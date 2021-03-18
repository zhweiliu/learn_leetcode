from typing import List

'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

'''


def reverse(x: int) -> int:
    singed = -1 if x < 0 else 1
    rev = 0
    based = 10
    posi_bound = (2 ** 31 - 1) / based
    neg_bound = (-2 ** 31) / based
    while x != 0:
        pop = x % 10

        if pop > 0 and singed < 0:
            pop -= 10

        x = int(x / 10)

        if rev > posi_bound or (rev == posi_bound and pop > 7):
            return 0

        if rev < neg_bound or (rev == neg_bound and pop < -8):
            return 0

        rev = rev * 10 + pop
    return rev


if __name__ == '__main__':
    x = -123
    print(reverse(x))
