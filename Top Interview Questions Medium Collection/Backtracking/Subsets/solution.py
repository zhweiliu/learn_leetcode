from typing import List, Dict, Set, Tuple

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
    - 1 <= nums.length <= 10
    - -10 <= nums[i] <= 10
    - All the numbers of nums are unique.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''


class Solution:

    def dfs(self, nums: List[int], index: int,  ret: List[List[int]], path: List[int]):
        ret.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, ret, path + [nums[i]])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        ret: List[List[int]] = []
        self.dfs(nums, 0, ret, [])

        return ret


if __name__ == '__main__':
    nums = [1, 2, 3]

    sol = Solution()
    print(f'{sol.subsets(nums)}')
