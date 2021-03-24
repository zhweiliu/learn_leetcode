from typing import List

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
    - 0 <= nums.length <= 3000
    - -10**5 <= nums[i] <= 10**5
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = set()
        for idx, val in enumerate(nums[:-2]):
            # val equals prev val
            if idx >= 1 and val == nums[idx-1]:
                continue

            d = {}
            for x in nums[idx+1:]:
                if x not in d:
                    d[-val-x] = 1
                else:
                    res.add((val, -val-x, x))
        return list(res)



if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]

    sol = Solution()
    print(sol.threeSum(nums))
