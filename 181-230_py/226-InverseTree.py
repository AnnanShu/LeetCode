# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode):
        the_root = root
        def swap(node, ):
            temp = node.left
            node.left = node.right
            node.right = temp
        if not root:
            return
        if root.left or root.right:
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            
            swap(root)
        return the_root
