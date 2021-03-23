from typing import List

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, \
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and \
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, \
return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 400
    
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''


class Solution:

    def rob(self, nums: List[int]) -> int:
        '''
        setup the initial nums[0] and nums[1], i.e. if len(nums) < 2 then output result direct,
        take max(nums[i-2] + nums[i], nums[i-1]) to iterate, and output last result by every round by max value
        :param prices:
        :return:
        '''

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        robprev = nums[0]
        robnext = max(nums[0], nums[1])

        for i in range(2, len(nums), 1):
            tmp = robprev
            robprev = robnext
            robnext = max(robprev, tmp + nums[i])

        return robnext


if __name__ == '__main__':
    nums = [2,1]

    sol = Solution()
    print(sol.rob(nums))
