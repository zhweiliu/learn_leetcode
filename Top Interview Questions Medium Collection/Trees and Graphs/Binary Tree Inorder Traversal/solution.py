from typing import List, Dict, Set

'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Follow up:
    - Recursive solution is trivial, could you do it iteratively?

Constraints:
    - The number of nodes in the tree is in the range [0, 100].
    - -100 <= Node.val <= 100

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack: List[TreeNode] = []
        ret = []

        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop(-1)
            ret.append(node.val)
            node = node.right

        return ret



def create_tree(tree_serial: List) -> List[TreeNode]:
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
    tree_serial = [1, None, 2, 3]
    tree = create_tree(tree_serial)
    root = tree[0]

    sol = Solution()
    ret = sol.inorderTraversal(root)

    print(ret)
