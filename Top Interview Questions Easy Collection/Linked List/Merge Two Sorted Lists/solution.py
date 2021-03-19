from typing import Tuple

'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Constraints:
    - The number of nodes in both lists is in the range [0, 50].
    - -100 <= Node.val <= 100
    - Both l1 and l2 are sorted in non-decreasing order.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    node = None
    prev_node = None
    root = None

    while (l1 or l2):
        if not l1:
            prev_node, node, l2 = node, l2, l2.next
        elif not l2:
            prev_node, node, l1 = node, l1, l1.next
        else:
            if l1.val < l2.val:
                prev_node, node, l1 = node, l1, l1.next
            else:
                prev_node, node, l2 = node, l2, l2.next

        if prev_node:
            prev_node.next = node

        if not root:
            root = node

    return root


if __name__ == '__main__':
    l1 = [1,3,4]
    l2 = [0]
    q1 = [ ListNode(ele) for ele in l1 ]
    q2 = [ ListNode(ele) for ele in l2 ]

    for i in range(0, len(q1) - 1, 1):
        q1[i].next = q1[i + 1]

    for i in range(0, len(q2) - 1, 1):
        q2[i].next = q2[i + 1]

    if len(q1) == 0:
        q1.append(None)

    if len(q2) == 0:
        q2.append(None)

    hl = mergeTwoLists(q1[0], q2[0])

    while hl:
        print(hl.val)
        hl = hl.next
