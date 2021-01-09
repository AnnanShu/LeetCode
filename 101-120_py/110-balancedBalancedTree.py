# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.isBalance = True
    def isBalanced(self, root: TreeNode) -> bool:
        def auxiliary(node):
            if node:
                left = auxiliary(node.left)
                right = auxiliary(node.right)
                if abs(left-right) > 1:
                    self.isBalance = False
                return max(left, right) + 1
            else:
                return 0

        auxiliary(root)
        return self.isBalance 