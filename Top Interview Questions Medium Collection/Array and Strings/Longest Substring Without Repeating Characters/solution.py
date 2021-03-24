from typing import List, Dict, Set

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/

Given a string s, find the length of the longest substring without repeating characters.


Constraints:
    - 0 <= s.length <= 5 * 10**4
    - s consists of English letters, digits, symbols and spaces.

    

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s :
            return 0

        # max_len: length of longest substring
        # count: currently length of substring
        max_len, count = 0, 0

        # left/right bound for slide window
        window_start, window_end = 0, 0

        # determine the character is duplicate or not
        char_set = set()

        # sliding window mask longest substring between s[window_start] to s[window_end]
        while window_end < len(s):

            char = s[window_end]

            if char not in char_set:
                char_set.add(char)
                count += 1
                max_len = max(max_len, count)
            else:
                # char duplicate with char_set
                # it is important that for capture length of substring, not capture a substring.
                while s[window_start] != s[window_end]:
                    char_set.remove(s[window_start])
                    window_start += 1
                    count -=1

                window_start+=1

            window_end+=1

        return max_len


if __name__ == '__main__':
    s = ""

    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
