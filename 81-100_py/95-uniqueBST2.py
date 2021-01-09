from collections import List
from collections import Iterable
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees_in(start, end):
            if start > end:
                return [None,]
            allTrees = []

            for i in range(start, end+1):
                leftTrees = generateTrees_in(start, i-1)
                rightTrees = generateTrees_in(i+1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        allTrees.append(TreeNode(i, l, r))
            
            return allTrees
        return generateTrees_in(1, n) if n else []
