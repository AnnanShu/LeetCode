class BinaryTree:
    def __init__(self, val=0):
        self.val = val
        self.leftChild = None
        self.rightChild = None




# we should use tree dynamic programming to solve this kind of problem 
# def nodeMaxSum(node):
#     sum = 0
#     leftmax = 0
#     rightmax = 0
#     if node.left is not None:
#         leftmax = node



def treeHeight(BinaryTree) -> int:
    left = 1
    right = 1
    if root.left:
        left =  treeHeight(root.left) + 1
    if root.right:
        right = treeHeight(root.right) + 1
    
    return max(left, right)

def nodeWidden(node):
    return treeHei

