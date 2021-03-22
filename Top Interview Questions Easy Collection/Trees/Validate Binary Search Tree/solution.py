from typing import List

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

Constraints:
    - The number of nodes in the tree is in the range [1, 104].
    - -2**31 <= Node.val <= 2**31 - 1

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def visit(self, node: TreeNode, low: int, high: int) -> bool:

        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return self.visit(
            node=node.left,
            low=low,
            high=node.val
        ) \
               & self.visit(
            node=node.right,
            low=node.val,
            high=high
        )

    def isValidBST(self, root: TreeNode) -> bool:
        return self.visit(root, low=-2 ** 31 -1, high=2 ** 31)


def create_tree(tree_serial: List) -> List[TreeNode]:
    # import math
    # for binary tree definition: depth of tree equals int(log2(len(root))) + 1
    # depth = math.log(len(root), 2) + 1

    tree = [TreeNode(ele) if ele is not None else None for ele in tree_serial]
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
    # root = [2,1,3]
    # root = [5,1,4,None,None,3,6]
    # root = [5, 4, 6, None, None, 3, 7]
    # root = [2147483647]
    root = [1,1]

    tree: List[TreeNode] = create_tree(tree_serial=root)

    sol = Solution()
    print(sol.isValidBST(tree[0]))
