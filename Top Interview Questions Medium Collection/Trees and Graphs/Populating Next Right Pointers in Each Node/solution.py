from typing import List, Dict, Set

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:
    - You may only use constant extra space.
    - Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Constraints:
    - The number of nodes in the given tree is less than 4096.
    - -1000 <= node.val <= 1000

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: 
    Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its \
    next right node, just like in Figure B. 
    
    The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def bfs(self, distance: int, ret: List[List['Node']]):

        if not ret[-1]:
            return

        while len(ret) <= (distance + 1) :
            ret.append([])

        if distance == 0:
            node = ret[distance][0]
            if node.left:
                node.left.next = node.right
                ret[distance + 1] += [node.left, node.right]
        else:
            prev_node = None
            for i in range(0, len(ret[distance])):
                node = ret[distance][i]
                if prev_node:
                    prev_node.next = node.left

                if node.left:
                    node.left.next = node.right
                    prev_node = node.right

                    ret[distance + 1] += [node.left, node.right]

        self.bfs(distance + 1, ret)

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        ret: List[List[Node]] = [[root]]
        self.bfs(0, ret)

        return root


def create_tree(tree_serial: List) -> List[Node]:
    tree = [Node(ele) if ele is not None else None for ele in tree_serial]
    for i in range(len(tree)):
        node_number = i + 1

        left_index = node_number * 2 - 1
        right_index = left_index + 1

        if not tree[i]:
            tree.insert(left_index, None)
            tree.insert(right_index, None)
            continue

        tree[i].left = tree[left_index] if left_index < len(tree) else None
        tree[i].right = tree[right_index] if right_index < len(tree) else None

    if len(tree) == 0:
        tree.append(None)

    return tree


if __name__ == '__main__':
    tree_serial = [0]
    tree = create_tree(tree_serial)
    root = tree[0]

    sol = Solution()
    root = sol.connect(root)

    ret = []
