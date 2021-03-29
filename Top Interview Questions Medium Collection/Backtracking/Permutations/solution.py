from typing import List, Dict, Set, Tuple

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Constraints:
    - 1 <= nums.length <= 6
    - -10 <= nums[i] <= 10
    - All the integers of nums are unique.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
'''


class Solution:

    def dfs(self, nums: List[int], ret: List[List[int]], path: List[int]):
        '''
        permute except self, recursive
        :param nums:
        :param ret:
        :param path:
        :return:
        '''
        if not nums:
            ret.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i+1:], ret, path + [nums[i]])

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        ret: List[List[int]] = []
        self.dfs(nums, ret, [])

        return ret


if __name__ == '__main__':
    nums = [1, 2, 3]

    sol = Solution()
    print(f'{sol.permute(nums)}')
