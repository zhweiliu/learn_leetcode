from typing import List, Dict, Set, Tuple

'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.


Note:
    - If the given node has no in-order successor in the tree, return null.
    - It's guaranteed that the values of the tree are unique.

Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 
    1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.


Example 2:
Input: root = [5,3,6,2,4,None,None,1], p = 6
Output: null
Explanation: 
    There is no in-order successor of the current node, so the answer is null.


'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:
            return None

        # if p at leaf with right subtree of root
        res: TreeNode = None

        while root:

            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right

        return res



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


def create_tree_with_p(tree_serial: List, p: int) -> (List[TreeNode], TreeNode):
    tree = [TreeNode(ele) if ele is not None else None for ele in tree_serial]
    p_node = None
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
        if tree[i].val == p:
            p_node = tree[i]

    if len(tree) == 0:
        tree.append(None)

    return tree, p_node


if __name__ == '__main__':

    tree_serial = [5, 3, 6, 2, 4, None, None, 1]
    p_value = 6
    tree, p = create_tree_with_p(tree_serial, p_value)
    root = tree[0]

    sol = Solution()
    inorder_root = sol.inorderSuccessor(root, p)
    print(f' in-order node value {inorder_root.val if inorder_root else None}')
