from typing import List, Dict, Set

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/

Given a string s, return the longest palindromic substring in s.

ref : https://medium.com/hoskiss-stand/manacher-299cf75db97e

Constraints:
    - 1 <= s.length <= 1000
    - s consist of only digits and English letters (lower-case and/or upper-case),

    

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        using manacher’s algorithm
        :param s:
        :return:
        '''
        string_size = len(s)

        # if length of s less than 3, LPS equals itself or empty
        if string_size < 3:
            if s == s[::-1]:
                return s
            else:
                return s[0]

        manacher_str = "#"

        # insert extra symbol into s
        for index in range(len(s)):
            manacher_str += s[index]
            manacher_str += "#"

        LPS_table = [0] * len(manacher_str)

        # let slide window initial center index be 1, left bound index be 0 and right bound index be 2
        center = 1
        max_right = 2
        max_length = 0

        # let LPS center initial center index be 0
        LPS_center = 0

        total_size = len(manacher_str)
        # visit all characters of manacher_str which is after insert extra symbol into s
        for index in range(1, len(manacher_str)):
            if index < max_right:
                # if index less than right bound index, i.e., current character at left side from right bound
                LPS_table[index] = min(LPS_table[2 * center - index], max_right - index)
            else:
                LPS_table[index] = 0

            # when calculating LPS value, self position (index) is not included
            while (index - LPS_table[index] - 1 >= 0 and
                   index + LPS_table[index] + 1 < total_size and
                   manacher_str[index - LPS_table[index] - 1] == manacher_str[index + LPS_table[index] + 1]):
                '''
                index - LPS_table[index] - 1 >= 0 : character in range between left and right bound
                index + LPS_table[index] + 1 < total_size : \
                    palindromic substring length always less or equals than manacher_str
                manacher_str[index - LPS_table[index] - 1] == manacher_str[index + LPS_table[index] + 1]: \
                    left bound distance to LPS center should be equals with right bound
                '''
                LPS_table[index] += 1

            # if palindromic substring length more than window size, than expansion window size
            if LPS_table[index] > max_length:
                max_length = LPS_table[index]
                LPS_center = index

            # if half of palindromic substring length more than half window size, than expansion window right bound
            if LPS_table[index] + index - 1 > max_right:
                max_right = LPS_table[index] + index - 1
                center = index
         
        start = int((LPS_center - max_length) / 2)
        return s[start: start + max_length]








if __name__ == '__main__':
    s = "babad"

    sol = Solution()
    print(sol.longestPalindrome(s))
