from typing import List, Dict

'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
    - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    - Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

'''


def isValidSudoku(board: List[List[str]]) -> bool:
    row_h: List[Dict] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    col_h: List[Dict] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    cube_h: List[Dict] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

    for row_idx in range(9):
        for col_idx in range(9):
            cube_idx = int(row_idx / 3) * 3 + int(col_idx / 3)

            num = board[row_idx][col_idx]

            if num == '.':
                continue

            if num in row_h[row_idx] or num in col_h[col_idx] or num in cube_h[cube_idx]:
                return False

            row_h[row_idx][num] = row_idx
            col_h[col_idx][num] = col_idx
            cube_h[cube_idx][num] = cube_idx

    return True


if __name__ == '__main__':
    board = [
        ["5", "3", "9", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(isValidSudoku(board))
