# Definition for a Node.
import collections
class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root 
        leftmost = root 
        while leftmost.left:
            head = leftmost 
            while head:
                # first conection:
                head.left.next = head.right
                # second connection
                if head.next:
                    head.right.next = head.next.right
                head = head.next

            leftmost = leftmost.left
        
        return root 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        Q = collections.deque([root,])
        while Q:    
            for i in range(len(Q)-1):
                cur_node = Q.popleft()
                cur_node.next = Q[0]
                if cur_node.left:
                    Q.append(cur_node.left)
                    Q.append(cur_node.right)
            
            cur_node = Q.popleft()
            cur_node.next = None 
            if cur_node.left:
                Q.append(cur_node.left)
                Q.append(cur_node.right)
        
        return root