from typing import Dict, List

'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.
'''


def firstUniqChar(s: str) -> int:
    exists_character = []

    for idx, c in enumerate(s):
        if c not in exists_character and c not in s[idx+1:]:
            return idx
        else:
            exists_character.append(c)

    return -1


if __name__ == '__main__':
    s = "leetcode"
    print(firstUniqChar(s))