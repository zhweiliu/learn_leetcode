from typing import List

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:

    - 0 ≤ x, y < 231



Example 1:
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_number = x ^ y
        count = 0
        while xor_number > 0:
            count += (xor_number & 1)
            xor_number >>= 1
        return count


if __name__ == '__main__':
    x = 7
    y = 4

    sol = Solution()
    print(sol.hammingDistance(x,y))

