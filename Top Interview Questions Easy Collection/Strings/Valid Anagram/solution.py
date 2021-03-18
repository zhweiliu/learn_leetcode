from typing import Dict, List

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''


def isAnagram(s: str, t: str) -> bool:
    '''
    compare the ascii value sum is different between string s and string t
    :param s:
    :param t:
    :return:
    '''
    # the 'ord' function can convert character to ascii value
    ascii_s = sum([ ord(c) for c in s])
    ascii_t = sum([ord(c) for c in t])

    # check intersection set if ascii value sum equals
    if ascii_s == ascii_t:
        return set(s).intersection(set(t)) == set(s)

    return ascii_s == ascii_t


if __name__ == '__main__':
    s = "ana"
    t = "nagaram"
    print(isAnagram(s,t))