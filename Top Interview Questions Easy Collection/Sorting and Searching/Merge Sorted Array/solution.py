from typing import List

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. 
You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

Constraints:
    - nums1.length == m + n
    - nums2.length == n
    - 0 <= m, n <= 200
    - 1 <= m + n <= 200
    - -109 <= nums1[i], nums2[i] <= 109
    
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if len(nums2) == 0:
            return

        # if nums2 exists elements
        for i in range(len(nums1)):
            if nums2 and nums1[i] == 0:
                nums1[i] = nums2.pop(0)
                m = m + 1

            for j in range(i, 0, -1):
                if nums1[j] < nums1[j - 1]:
                    nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]




if __name__ == '__main__':
    nums1 = [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
    m = 5
    nums2 = [-1, -1, 0, 0, 1, 2]
    n = 6


    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    print(nums1)
