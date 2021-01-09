# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        maximum_width = 1
        layer = list()
        number = list()
        if root.left:
            layer.append(root.left)
            number.append((1 << 1))
        if root.right:
            layer.append(root.right)
            number.append((1 << 1) + 1)
        while layer:
            n = len(layer)
            if n > 1:
                maximum_width = max(number[-1] - number[0] + 1, maximum_width )
            next_layer = list()
            next_number = list()
            for i in range(n):
                if layer[i].left:
                    next_layer.append(layer[i].left)
                    next_number.append((number[i] << 1))
                if layer[i].right:
                    next_layer.append(layer[i].right)
                    next_number.append((number[i] << 1) + 1)
            layer = next_layer
            number = next_number
            
        return maximum_width
                





(3 << 1) + 1