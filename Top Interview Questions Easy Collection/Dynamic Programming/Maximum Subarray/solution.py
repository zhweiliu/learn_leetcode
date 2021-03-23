from typing import List

'''
Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: 
    If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 
    which is more subtle.

Constraints:
    - 1 <= nums.length <= 3 * 10**4
    - -10**5 <= nums[i] <= 10**5
    
Example 1:
Input: nums = [1]
Output: 1

Example 2:
Input: nums = [5,4,-1,7,8]
Output: 23
'''


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        '''
        using Kadane's Algorithm
        https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98
        :param prices:
        :return:
        '''

        if len(nums) == 0:
            return 0

        max_ending_here = max_so_far = 0

        for n in nums:
            max_ending_here = max(0, max_ending_here+n)
            max_so_far = max(max_so_far, max_ending_here)

        # after Kadane's Algorithm, if max_so_far equals 0, means the all of values in nums list must less or equals 0
        # so take max values of nums list again
        if max_so_far == 0:
            max_so_far = max(nums)

        return max_so_far


if __name__ == '__main__':

    nums = [-2, -1]

    sol = Solution()
    print(sol.maxSubArray(nums))
