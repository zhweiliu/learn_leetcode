from typing import List, Dict, Set, Tuple

'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, \
where adjacent cells are horizontally or vertically neighboring. \
The same letter cell may not be used more than once.

Follow up: Could you use search pruning to make your solution faster with a larger board?

Constraints:
    - m == board.length
    - n = board[i].length
    - 1 <= m, n <= 6
    - 1 <= word.length <= 15
    - board and word consists of only lowercase and uppercase English letters.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.exit(board, word, x, y, 0):
                    return True
        return False

    def exit(self, board: List[List[str]], word: str, x: int, y: int, i: int):
        if i == len(word):
            return True
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        if board[y][x] != word[i]:
            return False

        board[y][x] = board[y][x].swapcase()

        isexit = self.exit(board, word, x + 1, y, i + 1) \
                 or self.exit(board, word, x, y + 1, i + 1) \
                 or self.exit(board, word, x - 1, y, i + 1) \
                 or self.exit(board, word, x, y - 1, i + 1)

        board[y][x] = board[y][x].swapcase()
        return isexit


if __name__ == '__main__':
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "SEE"

    sol = Solution()
    print(f'{sol.exist(board, word)}')
