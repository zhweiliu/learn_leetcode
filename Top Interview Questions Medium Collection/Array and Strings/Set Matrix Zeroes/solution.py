from typing import List

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
    - A straight forward solution using O(mn) space is probably a bad idea.
    - A simple improvement uses O(m + n) space, but still not the best solution.
    - Could you devise a constant space solution?

Constraints:
    - m == matrix.length
    - n == matrix[0].length
    - 1 <= m, n <= 200
    - -2**31 <= matrix[i][j] <= 2**31 - 1

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        is_col = False
        row_len = len(matrix)
        column_len = len(matrix[0])

        for i in range(row_len):

            # if zero value of element in first column
            if matrix[i][0] == 0:
                is_col = True

            # scan start by index 1 for each row
            for j in range(1, column_len):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # scan of each element and set to zero if first element is zero in row/column
        for i in range(1, row_len):
            for j in range(1, column_len):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # if origin-point have zero value, set zero value to first row
        if matrix[0][0] == 0:
            for j in range(column_len):
                matrix[0][j] = 0

        # if first column needs set zero
        if is_col:
            for i in range(row_len):
                matrix[i][0] = 0






if __name__ == '__main__':
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)
