from typing import List, Dict, Set, Tuple

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Constraints:
    - 1 <= n <= 8

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        ret = [('(', 1, 0)]

        while ret[0][1] < n or ret[0][2] < n:
            symbol, left, right = ret.pop(0)
            if left < n:
                ret.append((symbol + '(', left + 1, right))
            if right < n and left > right:
                ret.append((symbol + ')', left, right + 1))

        return [r[0] for r in ret]


if __name__ == '__main__':
    n = 1

    sol = Solution()
    print(f'{sol.generateParenthesis(n)}')
