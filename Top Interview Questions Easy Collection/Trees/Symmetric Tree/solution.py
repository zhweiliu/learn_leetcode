from typing import List

'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Constraints:
    - The number of nodes in the tree is in the range [1, 1000].
    - -100 <= Node.val <= 100
    
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Tips:
            1. left child value equals right child value
            2. left child value of left child equals right child value of right child
            3. right child value of left child equals right child value of left child
            4. return True if root is None
        """

        if not root:
            return True

        q = []

        q = q+ [root.left, root.right]

        while q:
            if len(q) < 2:
                return False

            l = q.pop(0)
            r = q.pop(0)

            if not l and not r:
                continue

            if not l or not r:
                return False

            if l.val != r.val:
                return False

            q += [ l.left, r.right, r.left, l.right]

        return True



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
    # root = [1,2,2,3,4,4,3]
    # root = [1,2,2,None,3,None,3]
    root = [1,2,2,4,3,3,4]
    tree: List[TreeNode] = create_tree(tree_serial=root)

    sol = Solution()
    print(sol.isSymmetric(tree[0]))
