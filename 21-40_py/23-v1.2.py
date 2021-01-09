# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        idx = range(len(lists))
        sorted_root = ListNode(0)
        current_node = sorted_root
        head_list = [lists[i].val for i in idx]
        while any(head_list):
            pass
        
        pass
