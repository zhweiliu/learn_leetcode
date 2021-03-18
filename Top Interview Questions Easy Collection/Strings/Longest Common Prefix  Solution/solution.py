from typing import Dict, List

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ''

    # take shortest string be common_prefix
    common_prefix: str = strs[0]
    for i in range(1, len(strs), 1):
        common_prefix = strs[i] if len(strs[i]) < len(common_prefix) else common_prefix

    for i in range(len(strs)):
        if strs[i] == common_prefix:
            continue

        compare_str: str = strs[i][:len(common_prefix)]
        for char_idx in range(len(common_prefix)):
            if common_prefix[char_idx] != compare_str[char_idx]:
                common_prefix = common_prefix[:char_idx]
                break

        if len(common_prefix) == 0:
            break

    return common_prefix


if __name__ == '__main__':
    strs = []
    print(longestCommonPrefix(strs))
