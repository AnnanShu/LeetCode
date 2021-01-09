# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        current_sum = 0
        the_sum = sum

        def auxiliary_func(node, current_sum):
            if not node:
                return False
            current_sum += node.val
            if not node.left and not node.right:
                return current_sum == the_sum

            else:
                return auxiliary_func(node.left, current_sum) | \
                    auxiliary_func(node.right, current_sum)


        return auxiliary_func(root, current_sum)

class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        else:
            return hasPathSum(root.left, sum-root.val) | \
                hasPathSum(root.right, sum-root.val)
