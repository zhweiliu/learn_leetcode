from typing import List

'''
Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:
    - Solution(int[] nums) Initializes the object with the integer array nums.
    - int[] reset() Resets the array to its original configuration and returns it.
    - int[] shuffle() Returns a random shuffling of the array.

Constraints:
    - 1 <= nums.length <= 200
    - -106 <= nums[i] <= 106
    - All the elements of nums are unique.
    - At most 5 * 104 calls will be made to reset and shuffle.

Tips:
    - The solution expects that we always use the original array to shuffle() else some of the test cases fail. 
        (Credits; @snehasingh31)
    
Example 1:
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally 
                            likely to be returned. Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
'''


class Solution:
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.reset()
    # param_2 = obj.shuffle()

    original_array: List[int] = []

    def __init__(self, nums: List[int]):
        self.original_array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original_array

    def shuffle(self) -> List[int]:
        """
        using random package and pop item from array, or you can see Fisher-Yates Algorithm
        Fisher-Yates Algorithm:
            https://gaohaoyang.github.io/2016/10/16/shuffle-algorithm/
        """
        import random
        tmp = self.original_array.copy()
        shuffle_array = []

        while tmp:
            shuffle_array.append(tmp.pop(random.randint(0, len(tmp)-1)))

        return shuffle_array





if __name__ == '__main__':
    acts = ["Solution", "shuffle", "reset", "shuffle"]
    nums = [1, 2, 3]
    sol = None
    for act in acts:
        if act == 'Solution':
            sol = Solution(nums=nums)
            print(f'create solution object with {nums}')
        elif act == 'shuffle':
            param_2 = sol.shuffle()
            print(f'Shuffle the array {sol.original_array} and return {param_2}')
        elif act == 'reset':
            param_1 = sol.reset()
            print(f'Resets the array back to original configuration {param_1}')
