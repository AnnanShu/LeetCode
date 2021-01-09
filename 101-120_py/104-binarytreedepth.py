# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        leftlen = 1
        rightlen = 1
        currentNode = root
        if root != None:
            if root.left != None:
                leftlen = self.maxDepth(currentNode.left) + 1
            if root.right != None:
                rightlen = self.maxDepth(currentNode.right) + 1
        else:
            return 0
            
        return max(leftlen, rightlen) 