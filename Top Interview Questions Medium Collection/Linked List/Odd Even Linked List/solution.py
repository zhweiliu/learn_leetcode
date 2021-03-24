from typing import List, Dict, Set

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even \
indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

Constraints:
    - The number of nodes in the linked list is in the range [0, 10**4].
    - -10**6 <= Node.val <= 10**6

Follow up: Could you solve it in O(1) space complexity and O(nodes) time complexity?
    

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd, even = head, head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head


def create_link_list(nums: List[int]) -> ListNode:
    if len(nums) == 0:
        return None

    node = ListNode(val=nums[0])
    root = node

    for i in range(1, len(nums), 1):
        node.next = ListNode(val=nums[i])
        node = node.next

    return root


if __name__ == '__main__':
    n = [2,1,3,5,6,4,7]

    head = create_link_list(n)

    sol = Solution()
    node = sol.oddEvenList(head)

    num = []

    while node:
        num.append(node.val)
        node = node.next

    print(num)