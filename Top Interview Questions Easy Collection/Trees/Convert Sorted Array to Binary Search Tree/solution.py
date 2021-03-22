from typing import List

'''
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by 
more than one.

Constraints:
    - 1 <= nums.length <= 104
    - -104 <= nums[i] <= 104
    - nums is sorted in a strictly increasing order.
    
Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def create_subtree(self, root: TreeNode, left: List[int], right: List[int]):
        '''
        Both left and right are sorted in a strictly increasing order
        :param root:
        :param left:
        :param right:
        :return:
        '''

        if len(left) > 0:
            l_mid_idx = int(len(left)/2)
            left_node = TreeNode(val=left[l_mid_idx])
            root.left = left_node

            self.create_subtree(
                left_node,
                left[:l_mid_idx],
                left[l_mid_idx + 1:] if len(left) > l_mid_idx + 1 else []
            )

        if len(right) > 0:
            r_mid_idx = int(len(right) / 2)
            right_node = TreeNode(val=right[r_mid_idx])
            root.right = right_node
            self.create_subtree(
                right_node,
                right[:r_mid_idx],
                right[r_mid_idx+1:] if len(right) > r_mid_idx + 1 else []
            )


    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        To solve this, we will follow these steps.
        1. If nums is empty, then return Null
        2. find the mid element, and make it root
        3. Divide the array into two sub-arrays, left part of the mid element, and right part of the mid element
        4. recursively perform the same task for the left subarray and right subarray.
        :param nums:
        :return:
        '''

        if not nums:
            return None

        # By default, nums is sorted in a strictly increasing order. Or we need to sort the nums by ascending in first time

        mid_value_idx = int(len(nums)/2)

        root = TreeNode(val=nums[mid_value_idx])
        self.create_subtree(
            root,
            nums[:mid_value_idx],
            nums[mid_value_idx+1:]
        )

        return root



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
    # nums = [-10,-3,0,5,9]
    nums = []

    # tree: List[TreeNode] = create_tree(tree_serial=root)

    sol = Solution()
    root = sol.sortedArrayToBST(nums)
    print('root')
