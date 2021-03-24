from typing import List, Dict, Set

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/

Given an integer array nums, return true \
if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. \
If no such indices exists, return false.

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

Constraints:
    - 1 <= nums.length <= 10**5
    - -2**31 <= nums[i] <= 2**31 - 1

    

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"
'''


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = 2**31-1

        # visit all num by index k
        for k in nums:
            # stop if i >= k, let i < k
            if i >= k:
                i = k
            # stop if j >= k, means i < j and k < j
            elif j >=k:
                j = k
            else:
            # i < j < k
                return True

        return False

if __name__ == '__main__':
    nums = [2,1,5,0,4,6]

    sol = Solution()
    print(sol.increasingTriplet(nums))
