from typing import List

'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
    - Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    - Could you do it in-place with O(1) extra space?
    
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


'''


def swap(nums: List[int], start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    nums_len = len(nums)

    # if nums_len < k, the rotate need follow by nums_len
    k %= nums_len

    # first, reverse all nums by swap
    swap(nums, 0, nums_len - 1)

    # second, reverse of k element by swap
    swap(nums, 0, k - 1)

    # in the end, reverse last n-k
    swap(nums, k, nums_len - 1)


if __name__ == '__main__':
    nums = [-1,-100,3,99]
    k = 3

    rotate(nums, k)
    print(nums)
