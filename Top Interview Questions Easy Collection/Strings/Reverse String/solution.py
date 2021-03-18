from typing import List

'''
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Follow up: 
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) 
    extra memory.
'''


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start, end = 0, len(s) - 1
    # rotate elements by middle index
    while start < end:
        s[start], s[end] = s[end], s[start]
        start, end = start + 1, end - 1


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)
