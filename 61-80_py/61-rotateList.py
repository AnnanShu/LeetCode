class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        p = q = r = head 
        n = 1
        # calculate the total length of the list 
        while r.next:
            n += 1
            prev = r
            r = r.next

        k = k % n 
        if k == 0: return head 
        for _ in range(k):
            p = p.next
        prev = None 
        while p:
            p = p.next
            prev = q
            q = q.next
        # connect tail to head     
        r.next = head 
        prev.next = None 
        return q