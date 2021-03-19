from typing import Tuple

'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
    - The number of nodes in the list is the range [0, 5000].
    - -5000 <= Node.val <= 5000

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def swap_direct(node: ListNode) -> Tuple:
    root = None
    if node.next:
        swap_node, root = swap_direct(node.next)
        swap_node.next = node
        node.next = None
    else:
        root = node

    return node, root


def reverseList(head: ListNode) -> ListNode:
    if head:
        node, root = swap_direct(head)
    else:
        root = head
    return root


if __name__ == '__main__':
    serial = [1, 2, 3, 4, 5]
    q = [ListNode(ele) for ele in serial]
    for i in range(0, len(q) - 1, 1):
        q[i].next = q[i + 1]

    hl = reverseList(q[0])

    while hl:
        print(hl.val)
        hl = hl.next
