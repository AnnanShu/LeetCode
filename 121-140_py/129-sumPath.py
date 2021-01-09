# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(path, cur_node):
            if not cur_node:
                nonlocal res 
                res += int(''.join(path[:]))
                return 
            else:
                
                for nxt in [cur_node.left, cur_node.right]:
                    path.append(cur_node)
                    dfs(path, nxt)
                    path.pop()
        
        res = 0
        dfs([], root)
        return res