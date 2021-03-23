from typing import List

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Constraints:
    - 1 <= s.length <= 10**4
    - s consists of parentheses only '()[]{}'.

Example 1:
Input: s = "()"
Output: true
    
Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
'''


class Solution:
    rules = {
        '}': '{',
        ']': '[',
        ')': '(',
    }

    def isValid(self, s: str) -> bool:
        stack: List[str] = []

        for symbol in s:
            if symbol in ['(', '[', '{']:
                stack.append(symbol)

            elif symbol in [')', ']', '}']:
                if not stack or self.rules[symbol] != stack.pop(-1):
                    return False
        return False if stack else True


if __name__ == '__main__':
    s = ']'

    sol = Solution()
    print(sol.isValid(s))
