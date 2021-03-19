from typing import Tuple

'''
Given the head of a singly linked list, return true if it is a palindrome.

Constraints:
    - The number of nodes in the list is in the range [1, 105].
    - 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    rev = None

    # fast go ahead by 2 step and slow go ahead by 1 step
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        # let slow go ahead by 1 step, and the rev be reverse linked list through slow
        rev, rev.next, slow = slow, rev, slow.next

    # if fast exists, means linked list have odd elements, then the slow should be go to next
    if fast:
        slow = slow.next

    # check is value different between rev and slow
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next

    # if values of rev linked list equals the slow linked list, the rev will be None, or exists if not equals
    return not rev



if __name__ == '__main__':
    head = [1,2,1,2,2,1]
    q1 = [ ListNode(ele) for ele in head ]

    for i in range(0, len(q1) - 1, 1):
        q1[i].next = q1[i + 1]

    if len(q1) == 0:
        q1.append(None)

    print(isPalindrome(q1[0]))
