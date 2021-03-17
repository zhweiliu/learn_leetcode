from typing import List

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear 
as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

'''

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    intersect_set = set(nums1).intersection(set(nums2))
    bucket = {
        its: min(nums1.count(its), nums2.count(its))
        for its in intersect_set
    }

    intersect_set = []
    for its in bucket:
        intersect_set = intersect_set + ([its] * bucket[its])
    return intersect_set


def intersect_2(nums1: List[int], nums2: List[int]) -> List[int]:
    bucket = {}
    for num in nums1:
        if num not in bucket:
            bucket[num] = 0
        bucket[num] += 1

    intersect_set = []
    for num in nums2:
        if num in bucket and bucket[num] > 0:
            intersect_set.append(num)
            bucket[num] -= 1

    return intersect_set


if __name__ == '__main__':
    nums1 = [9, 4, 9, 8, 4]
    nums2 = [4, 9, 5, 4]
    print(intersect_2(nums1, nums2))
    print(intersect_2(nums2, nums1))
