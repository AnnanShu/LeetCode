class TreeNode:
    pass
class Solution:
    def __init__(self):
        self.pres = {}

    def rob(self, root: TreeNode):
        if not root:
            return 0
        if root in self.pres:
            return self.pres[root]
        self.pres[root] = max(self.rob(root.left)+self.rob(root.right),\
             root.val+(0 if not root.left else self.rob(root.left.left)+ \
                 self.rob(root.left.right))+(0 if not root.right else \
                     self.rob(root.right.left)+self.rob(root.right.right)))
        return self.pres[root]

"3".lower().islower()