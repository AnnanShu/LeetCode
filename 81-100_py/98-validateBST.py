# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if root.left and root.right:           
#             if root.left.val < root.val and root.right.val > root.val:
#                 return self.isValidBST(root.left) and self.isValidBST(root.right)
#             else:
#                 return False

#         elif root.left:
#             if root.left.val < root.val:
#                 return self.isValidBST(root.left)
#             else:
#                 return False
#         elif root.right:
#             if root.right.val > root.val:
#                 return self.isValidBST(root.right)
#             else:
#                 return False
#         else:
#             return True

float('-inf') < 5

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, lower = float('-inf'), upper=float('inf')):

            