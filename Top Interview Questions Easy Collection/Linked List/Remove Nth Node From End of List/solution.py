from typing import Dict, List

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Constraints:
    - The number of nodes in the list is sz.
    - 1 <= sz <= 30
    - 0 <= Node.val <= 100
    - 1 <= n <= sz

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node = head
    # use list be queue
    node_queue = []
    while node:
        '''
        the node queue keep node amount of n and order by last, last-1, last-2, ..., last-n-1 
        '''
        if len(node_queue) == n + 1:
            node_queue.pop(0)
        node_queue.append(node)
        node = node.next


    # if target is head
    if node_queue[len(node_queue) - n] == head:
        head = node_queue[len(node_queue) - n].next

    # target always in node_queue[1], node_queue[0] is previous node with target node
    node_queue[0].next = node_queue[0].next.next if node_queue[0].next else None

    return head


if __name__ == '__main__':
    serial = [1,2,3,4,5]
    q = [ListNode(ele) for ele in serial]
    for i in range(0, len(q) - 1, 1):
        q[i].next = q[i + 1]

    n = 2

    head = removeNthFromEnd(q[0], n)

    while head:
        print(head.val)
        head = head.next
