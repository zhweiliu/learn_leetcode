from typing import List

def reverse(nums: List, start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start+1, end-1

def transpost(matrix: List[List[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix), 1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def rotate(matrix: List[List[int]]) -> None:
    transpost(matrix)
    for row in matrix:
        reverse(row, 0, len(row)-1)




if __name__ == '__main__':
    matrix = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]

    rotate(matrix)
    print(matrix)

''' if reflect and then transpose
5 4 3 2 1
10 9 8 7 6
15 14 13 12 11
20 19 18 17 16
25 24 23 22 21

5 10 15 20 25
4 9 14 19 24
3 8 13 18 23
2 7 12 17 22
1 6 11 16 21
'''