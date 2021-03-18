from typing import Dict, List

'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''


def isPalindrome(s: str) -> bool:
    # keep alpha characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalpha() or c.isdigit())
    start, end = 0, len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start, end = start + 1, end - 1

    return True


if __name__ == '__main__':
    s = "0P"
    print(isPalindrome(s))
