from typing import List

'''
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Constraints:
    - The number of nodes in the tree is in the range [0, 2000].
    - -1000 <= Node.val <= 1000
    
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        values = []
        q = [root]

        while q:
            values.append([node.val for node in q])
            next_layer = []
            for node in q:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            q = next_layer

        return values


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
    # root = [3,9,20,None,None,15,7]
    # root = [1]
    root = [1, 2, None, 3, None, 4, None, 5]

    tree: List[TreeNode] = create_tree(tree_serial=root)

    sol = Solution()
    print(sol.levelOrder(tree[0]))
