from typing import List, Dict, Set, Tuple

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''


class Solution:

    def dfs(self, grid: List[List[str]], visited: List[List[bool]], i: int, j: int):
        if i > -1 and j > -1 and i < len(grid) and j < len(grid[0]) and not visited[i][j] and grid[i][j] == '1':

            visited[i][j] = True
            self.dfs(grid, visited, i + 1, j)
            self.dfs(grid, visited, i - 1, j)
            self.dfs(grid, visited, i, j + 1)
            self.dfs(grid, visited, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        using dfs to found islands
        '''

        if not grid or not grid[0]:
            return 0

        visited = [ [False] * len(grid[0]) for _ in range(len(grid)) ]
        ret = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, visited, i, j)
                    ret += 1

        return ret


if __name__ == '__main__':
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

    sol = Solution()
    print(f'number of island {sol.numIslands(grid)}')
