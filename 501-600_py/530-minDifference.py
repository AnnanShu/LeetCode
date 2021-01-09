class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min_diff = float('inf')
        prev = float('inf')
        def in_order(root):
            if root:
                in_order(root.left)
                nonlocal min_diff, prev
                cur = root.val 
                min_diff = min(abs(cur - prev), min_diff)
                prev = cur 
                in_order(root.right)
                 
        in_order(root)
        return min_diff