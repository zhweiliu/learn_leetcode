from typing import List, Dict, Set

'''
Given a sorted integer array nums, where the range of elements are in
the inclusive range [lower, upper], return its missing ranges.

Example 1:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

'''



class Solution:
    MAX_VALUE = 2**31-1

    def getRange(self, num1: int, num2: int) -> str:
        return str(num1) if num1 == num2 else f'{num1}->{num2}'

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        ret = []

        # if lower equals max value, then return empty result
        if lower == self.MAX_VALUE:
            return ret

        # let next equals lower
        next = lower

        # visit all num of nums list
        for num in nums:

            # if num less than next, skip current round in loop
            if num < next:
                continue

            # if num equals next, update the next value to num + 1
            if num == next:
                next += 1
                continue

            # if the num value not in [next, num-1], that is a range of target need to output
            ret.append(self.getRange(next, num-1))

            # if the num value equals max value, means num value range touch the bound, os it can output
            if num == self.MAX_VALUE:
                return ret

            # update the next value to num+1
            next = num+1

        #after visit all num value in nums list, of next less than or equals upper,
        # means it exists some range after nums[-1] value to upper
        if next <= upper:
            ret.append(self.getRange(next, upper))

        return ret



if __name__ == '__main__':
    nums =[0, 1, 3, 50, 75]
    lower = 0
    upper = 99

    sol = Solution()
    ret = sol.findMissingRanges(nums, lower, upper)

    print(ret)