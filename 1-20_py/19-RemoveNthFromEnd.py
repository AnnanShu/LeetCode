# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = head
        list1 = start
        list2 = start
        for _ in range(n):
            list2 = list2.next
        while list2.next != None:
            list1 = list1.next
            list2 = list2.next
        list1.next = list1.next.next
        return start
        

def main():
    l1 = [1]
    n =1
    start = ListNode()
    for each in l1:
        current.val = each
        current.next = ListNode

if __name__ == '__main__':
    main()
    
