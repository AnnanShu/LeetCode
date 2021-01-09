from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # bst generator
        def bstgen(root):
            if root:
                yield from bstgen(root.left)
                yield root
                yield from bstgen(root.right)
        g1, g2 = bstgen(root1), bstgen(root2)
        v1, v2 = next(g1, None), next(g2, None)
        ans = []
        while v1 and v2:
            if v1.val >= v2.val:
                ans.append(v2.val)
                v2 = next(g2, None)
            else:
                ans.append(v1.val)
                v1 = next(g1, None)

        v = v1 or v2 
        g = g1 if v1 else g2 
        while v:
            ans.append(v.val)
            v = next(g, None)
        return ans 