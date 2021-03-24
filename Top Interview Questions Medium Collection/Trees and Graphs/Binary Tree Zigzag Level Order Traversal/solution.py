from typing import List, Dict, Set

'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Constraints:
    - The number of nodes in the tree is in the range [0, 2000].
    - -100 <= Node.val <= 100

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [[1]]

Example 4:
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
    def dfs(self, node: TreeNode, depth: int, ret: List[List[int]]):
        if node is None:
            return

        while len(ret) <= depth:
            ret.append([])

        if depth % 2 == 0 :
            ret[depth].append(node.val)
        else:
            ret[depth].insert(0,node.val)

        self.dfs(node.left, depth+1, ret)
        self.dfs(node.right, depth+1, ret)

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret: List[List[int]] = []
        self.dfs(root, 0, ret)
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
    tree_serial = []
    tree = create_tree(tree_serial)
    root = tree[0]

    sol = Solution()
    ret = sol.zigzagLevelOrder(root)

    print(ret)
