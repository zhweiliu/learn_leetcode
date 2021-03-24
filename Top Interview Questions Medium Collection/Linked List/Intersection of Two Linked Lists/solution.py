from typing import List, Dict, Set

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1: see example of above url link

It is guaranteed that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?

Constraints:
    - The number of nodes of listA is in the m.
    - The number of nodes of listB is in the n.
    - 0 <= m, n <= 3 * 104
    - 1 <= Node.val <= 105
    - 0 <= skipA <= m
    - 0 <= skipB <= n
    - intersectVal is 0 if listA and listB do not intersect.
    - intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB intersect.
 

Follow up: Could you solve it in O(1) space complexity and O(nodes) time complexity?
    

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: 
    The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
    There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: 
    The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
    From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
    There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
    
Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: 
    From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. 
    Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
    Explanation: The two lists do not intersect, so return null.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        using Two Pointers
        Time complexity : O(N + M)O(N+M).
        Space complexity : O(1)O(1).
        :param headA:
        :param headB:
        :return:
        '''

        node_a = headA
        node_b = headB

        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else headA

        return node_a




def create_link_list(nums: List[int]) -> ListNode:
    if len(nums) == 0:
        return None

    node = ListNode(val=nums[0])
    root = node

    for i in range(1, len(nums), 1):
        node.next = ListNode(val=nums[i])
        node = node.next

    return root


def create_intersection_link_list(
        listA: List[int],
        listB: List[int],
        skipA: int,
        skipB: int,
        intersectionVal: int
) -> (ListNode, ListNode):
    if intersectionVal > 0:
        node_a = create_link_list(listA[:skipA])
        node_b = create_link_list(listB[:skipB])

        intersect = create_link_list(listA[skipA:])
        a, b = node_a, node_b
        while a.next:
            a = a.next
        a.next = intersect

        while b.next:
            b = b.next
        b.next = intersect

        return (node_a, node_b, intersect)
    else:
        return (create_link_list(listA), create_link_list(listB), None)

if __name__ == '__main__':
    listA = [2,6,4]
    listB = [1,5]
    skipA = 3
    skipB = 2
    intersectVal = 0

    headA, headB, intersec_node = create_intersection_link_list(
        listA, listB, skipA, skipB, intersectVal
    )


    sol = Solution()
    node = sol.getIntersectionNode(headA, headB)

    print(f'intersection value {node.val if node else None} and { "" if node == intersec_node else "not "}passed ')