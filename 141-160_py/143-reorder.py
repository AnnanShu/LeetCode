import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        Q = collections.deque()
        while head:
            Q.append(head)
            head = head.next
        dummy = ListNode(0)
        while Q:
            dummy.next = Q.popleft()
            dummy = dummy.next
            if Q:
                dummy.next = Q.pop()
                dummy = dummy.next
        dummy.next = None 
        
        return head 
                