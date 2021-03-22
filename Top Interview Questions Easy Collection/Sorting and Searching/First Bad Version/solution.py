from typing import List

'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Constraints:
    - 1 <= bad <= n <= 231 - 1
    
Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
'''

version_list = []

def isBadVersion(version: int) -> bool:
    '''
    Demo isBadVersion functional, but this function build-in leetcode.
    :param version:
    :return:
    '''
    return version_list[version]



class Solution:
    def firstBadVersion(self, n):
        """
        using binary search find out first bad version
        :type n: int
        :rtype: int
        """
        if n < 1:
            n = 1

        if n > 2**31 -1:
            n = 2**31-1

        left, right = 1, n
        while left < right:
            mid: int = int(left + (right-left) / 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left





if __name__ == '__main__':

    n = 1
    bad = 1
    version_list = [ False if _ < bad else True for _ in range(n)]

    print(f'version_list {version_list}')

    sol = Solution()
    print(f'first bad version : {sol.firstBadVersion(n)} ')
