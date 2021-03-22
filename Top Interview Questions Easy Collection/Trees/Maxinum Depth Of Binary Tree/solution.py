from typing import List

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:
    - The number of nodes in the tree is in the range [0, 104].
    - -100 <= Node.val <= 100

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def visit(self, node: TreeNode):
        depth = 1

        if not node:
            return 0

        return depth + max(self.visit(node.left), self.visit(node.right))

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(
            self.visit(root.left),
            self.visit(root.right)
        )


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
    root = [3,4,5,-7,-6,None,None,-7,None,-5,None,None,None,-4]
    tree: List[TreeNode] = create_tree(tree_serial=root)

    sol = Solution()
    print(sol.maxDepth(tree[0]))
