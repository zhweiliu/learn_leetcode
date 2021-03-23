from typing import List

'''
Count the number of prime numbers less than a non-negative number, n.

Constraints:
    - 0 <= n <= 5 * 106

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

'''


class Solution:
    def countPrimes(self, n: int) -> int:
        # if n less than 2, no prime numbers here
        if n < 2:
            return 0

        # initial all state be 1.  1 be prime, 0 be non-prime
        exists_prime_nums = [1] * n

        # let number 0 and 1 be non-prime
        exists_prime_nums[0] = exists_prime_nums[1] = 0

        # count from 2 to sqrt(n)+1
        for i in range(2, int(n**0.5)+1, 1):
            # if not have modification by above numb
            if exists_prime_nums[i]:
                # Let the multiple of i be 0
                exists_prime_nums[i*i: n: i] = [0] * ( (n-1-i*i)//i+1 )

        return sum(exists_prime_nums)

if __name__ == '__main__':
    n = 100

    sol = Solution()
    print(sol.countPrimes(n))

