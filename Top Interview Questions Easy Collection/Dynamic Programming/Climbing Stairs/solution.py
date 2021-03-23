from typing import List

'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:
    - 1 <= n <= 45
    
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:

    fib = {
        1: 1,
        2: 2,
    }

    def climbStairs(self, n: int) -> int:
        '''
        using fibonacci number and hash table
        :param n:
        :return:
        '''

        if n in self.fib:
            return self.fib[n]

        self.fib[ n ] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.fib[n]


    def climbStairs_BinetsMethod(self, n: int) -> int:
        '''
        using Binet's Method
        This is an interesting solution which uses matrix multiplication to obtain the n-th Fibonacci Number.
        :param n:
        :return:
        '''
        basis: List[List[int]] = [ [1,1], [1,0]]
        matrix: List[List[int]] = self.BinetsMethodPow(basis, n)
        return matrix[0][0]

    def BinetsMethodPow(self, matrix: List[List[int]], n: int) -> List[List[int]]:
        ret: List[List[int]] = [ [1,0], [0,1] ]
        while n > 0:
            if n & 1 == 1:
                ret = self.BinetsMethodMatrixMultiply(ret, matrix)
            n >>= 1
            matrix = self.BinetsMethodMatrixMultiply(matrix, matrix)
        return ret


    def BinetsMethodMatrixMultiply(self, matrix_qn: List[List[int]], matrix_prev_qn: List[List[int]]) -> List[List[int]]:
        m: List[List[int]] = [[0,0], [0,0]]
        for i in range(2):
            for j in range(2):
                m[i][j] = matrix_qn[i][0] * matrix_prev_qn[0][j] +  matrix_qn[i][1] * matrix_prev_qn[1][j]
        return m


if __name__ == '__main__':

    n = 45

    sol = Solution()
    print(f'There are {sol.climbStairs_BinetsMethod(n)} ways to climb to the top.')
