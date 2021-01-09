# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2:
    def maxPathSum(self, root: TreeNode) -> int:
        path_sum = list()
        def max_sum(node:TreeNode, the_number = 0):
            if not node:
                return 0
            else:
                return node.val + max(max_sum(node.left), max_sum(node.right))

        def auxiliary_func2(node):
            return node.val + max_sum(node.left) + max_sum(node.right)

        def auxiliary_func(node):
            path_sum.append(auxiliary_func2(node))
            if node.left:
                path_sum.append(auxiliary_func2(node.left))
            if node.right:
                path_sum.append(auxiliary_func2(node.right))
        

        auxiliary_func(root)

        return max(path_sum)

class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
    def maxPathSum(self, root:TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            priceNewPath = node.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, priceNewPath)
            
            return node.val + max(leftGain, rightGain)
        
        maxGain(root)
        return self.maxSum
            

100 // 101
