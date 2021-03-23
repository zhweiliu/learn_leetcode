from typing import List

'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/601/

Constraints:
    - 1 <= numRows <= 30

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
Example 2:
Input: numRows = 1
Output: [[1]]
'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        base = [[1], [1,1]]
        if numRows < 3:
            return base[:numRows]

        # triangle row
        for i in range(2, numRows, 1):
            base.append([1, ])
            # column in row
            for j in range(1, i, 1):
                base[i].append( base[i-1][j-1] + base[i-1][j] )
            base[i].append(1)

        return base





if __name__ == '__main__':
    numRows = 6

    sol = Solution()
    print(sol.generate(numRows))

