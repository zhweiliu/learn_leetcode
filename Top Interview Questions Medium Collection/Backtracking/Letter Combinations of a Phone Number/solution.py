from typing import List, Dict, Set, Tuple

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/

Given a string containing digits from 2-9 inclusive, \ 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Constraints:
    - 0 <= digits.length <= 4
    - digits[i] is a digit in the range ['2', '9'].

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

'''


class Solution:
    letter_words = {
        '2': ['a', 'b', 'c', ],
        '3': ['d', 'e', 'f', ],
        '4': ['g', 'h', 'i', ],
        '5': ['j', 'k', 'l', ],
        '6': ['m', 'n', 'o', ],
        '7': ['p', 'q', 'r', 's', ],
        '8': ['t', 'u', 'v', ],
        '9': ['w', 'x', 'y', 'z', ],
    }

    def addLetter(self, digits: str, word: str, ret: List[str]):
        if not digits:
            if word:
                ret.append(word)
        else:
            for i in range(len(self.letter_words[digits[0]])):
                l = self.letter_words[digits[0]][i]
                self.addLetter(digits[1:], word + l, ret )

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        ret = []

        self.addLetter(digits, '', ret)

        return ret


if __name__ == '__main__':
    digits = "23"

    sol = Solution()
    print(f'{sol.letterCombinations(digits)}')
