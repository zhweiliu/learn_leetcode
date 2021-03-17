from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for idx, val in enumerate(nums):
        remain_value = target - val
        if remain_value in hashmap:
            return [hashmap[remain_value], idx]
        else:
            hashmap[val] = idx


if __name__ == '__main__':
    nums = [3,3]
    target = 9
    # print(plusOne(digits))
    print(twoSum(nums, target))
