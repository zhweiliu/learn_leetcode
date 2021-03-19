from typing import Tuple

'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is 
connected to. Note that pos is not passed as a parameter. 

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:
    - The number of the nodes in the list is in the range [0, 104].
    - -105 <= Node.val <= 105
    - pos is -1 or a valid index in the linked-list.
    
Follow up: Can you solve it using O(1) (i.e. constant) memory?

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def hasCycle(head: ListNode) -> bool:
    # Floyd's Cycle Finding Algorithm

    if not head:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False

        fast = fast.next.next
        slow = slow.next

    return True


if __name__ == '__main__':
    head = [3,2,0,-4]
    pos = 0
    q1 = [ ListNode(ele) for ele in head ]

    for i in range(0, len(q1) - 1, 1):
        q1[i].next = q1[i + 1]

    if pos > -1:
        q1[-1].next = q1[pos]

    if len(q1) == 0:
        q1.append(None)

    print(hasCycle(q1[0]))
