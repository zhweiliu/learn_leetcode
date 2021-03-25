from typing import List, Dict, Set

'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Follow up:
    If the BST is modified often (i.e., we can do insert and delete operations) and \
    you need to find the kth smallest frequently, how would you optimize


Constraints:
    - The number of nodes in the tree is n.
    - 1 <= k <= n <= 10**4
    - 0 <= Node.val <= 10**4

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        using in-order
        '''

        stack: List[TreeNode] = []
        ret = []

        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop(-1)
            ret.append(node.val)

            if len(ret) == k:
                return node.val

            node = node.right

        # if len(self.inorder) < k, means not found
        return None







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
    tree_serial = [4,2,5,None,3]
    tree = create_tree(tree_serial)
    root = tree[0]
    k = 1

    sol = Solution()
    found_num = sol.kthSmallest(root, k)

    print(f'found_num {found_num}')