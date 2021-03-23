from typing import List

'''
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x

Follow up: Could you solve it without loops/recursion?

Constraints:
    - -2**31 <= n <= 2**31 - 1

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Example 4:
Input: n = 45
Output: false

'''


class Solution:
    def isPowerOfThreeByDivide(self, n: int) -> bool:
        '''
        using loop to divide n with 3
        :param n:
        :return:
        '''
        if n < 1:
            return False

        if n == 1:
            return True

        while n > 1:
            n /= 3
            if n == 1:
                return True

        return False

    def isPowerOfThree(self, n: int) -> bool:
        '''
        using by integer limitation
        :param n:
        :return:
        '''
        if n < 1:
            return False

        if n == 1:
            return True

        max_value = 2**31 -1

        max_three_pow_value = next = 1
        while next < max_value:
            max_three_pow_value = next
            next *= 3

        return max_three_pow_value % n == 0


if __name__ == '__main__':
    n = 3**11

    sol = Solution()
    print(sol.isPowerOfThree(n))

