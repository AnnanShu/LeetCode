# Definition for singly-linked list.
'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 
0 itself.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        dummy = p = ListNode(None)          
        s = 0               # 初始化进位 s 为 0
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)  
            p.next = ListNode(s % 10)       # p.next 指向新链表, 用来创建一个新的链表
            p = p.next                      # p 向后遍历
            s //= 10                        # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None    # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None    # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next 


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # get a pointer point to head of the list
        res_head = ListNode(0)
        res = res_head
        val_1 = l1.val
        val_2 = l2.val
        if val_1 + val_2 > 9:
            # give one number next
            res.next = ListNode(1)
            res.val = (val_1 + val_2) % 10
        else:
            res.val = (val_1 + val_2)
     
        l1 = l1.next
        l2 = l2.next
        while(l1!=None or l2!=None):

            # if no number exceed: add a empty position
            if res.next == None:
                res.next = ListNode(0)
            
            # point res to next
            res = res.next
            if l1 != None and l2 != None:
                val_1 = l1.val
                val_2 = l2.val
                if val_1 + val_2 + res.val > 9:
                    # give one number next
                    res.next = ListNode(1)
                    res.val = (res.val + val_1 + val_2) % 10
                    l1 = l1.next
                    l2 = l2.next
                else:
                    res.val = res.val + val_1 + val_2
                    l1 = l1.next
                    l2 = l2.next
                    
            elif l1 != None:
                val_1 = l1.val
                if val_1 + res.val > 9:
                    res.next = ListNode(1)
                    res.val = (res.val + val_1) % 10
                    l1 = l1.next
                else:
                    res.val += val_1
                    l1 = l1.next


            else:
                val_2 = l2.val
                if val_2 + res.val > 9:
                    res.next = ListNode(1)
                    res.val = (res.val + val_2) % 10
                    l2 = l2.next
                else:
                    res.val = res.val + val_2
                    l2 = l2.next
                
                
        # return the head of the number
        return res_head



class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            p.next = ListNode((v1 + v2 + carry) % 10)
            carry = (v1 + v2 + carry) // 10
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
            p = p.next
        
        return dummy.next

    

        