# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if root:
            result = [[root.val, ], ]
            node_list = list()
            if root.left:
                node_list.append(root.left)
            if root.right:
                node_list.append(root.right)
        else:
            return []

        while node_list:
            node_list_inner = []
            sub_result = []
            for node in node_list:
                sub_result.append(node.val)
                if node.left:
                    node_list_inner.append(node.left)
                if node.right:
                    node_list_inner.append(node.right)

            node_list = node_list_inner
            result.append(sub_result)

        return result

