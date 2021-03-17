from typing import List, Dict


def isValidSudoku(board: List[List[str]]) -> bool:
    row_h: List[Dict] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    col_h: List[Dict] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    cube_h: List[Dict] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

    for row_idx in range(9):
        for col_idx in range(9):
            cube_idx = int(row_idx/3) * 3 + int(col_idx/3)

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