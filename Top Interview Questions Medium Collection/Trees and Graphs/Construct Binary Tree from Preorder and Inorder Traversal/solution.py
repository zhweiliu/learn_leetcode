from typing import List, Dict, Set

'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and \
inorder is the inorder traversal of the same tree, construct and return the binary tree

Constraints:
    - 1 <= preorder.length <= 3000
    - inorder.length == preorder.length
    - -3000 <= preorder[i], inorder[i] <= 3000
    - preorder and inorder consist of unique values.
    - Each value of inorder also appears in preorder.
    - preorder is guaranteed to be the preorder traversal of the tree.
    - inorder is guaranteed to be the inorder traversal of the tree

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        node = TreeNode(preorder.pop(0))

        subtree_left = inorder[:inorder.index(node.val)]

        if subtree_left:
            node.left = self.buildTree(preorder, subtree_left)

        subtree_right = inorder[inorder.index(node.val):]
        subtree_right.pop(0)
        if subtree_right:
            node.right = self.buildTree(preorder, subtree_right)

        return node




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
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    sol = Solution()
    root = sol.buildTree(preorder, inorder)

    ret = []


