from typing import List, Dict, Set

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Constraints:
    - 1 <= strs.length <= 10**4
    - 0 <= strs[i].length <= 100
    - strs[i] consists of lower-case English letters.
    

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h: Dict[str, List] = {}

        for s in strs:
            w_h = {}
            for c in s:
                if c not in w_h:
                    w_h[c] = 0
                w_h[c] += 1

            keys = sorted(w_h.keys())

            words = ''.join([ f'{w_h[k]}{k}' for k in keys])
            if words not in h:
                h[words] = []
            h[words].append(s)

        return [ v for v in h.values() ]





if __name__ == '__main__':
    strs = ["ddddddddddg","dgggggggggg"]

    sol = Solution()
    print(sol.groupAnagrams(strs))
