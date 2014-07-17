# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        
        dummy, carry = ListNode(-1), 0
        head = dummy
        
        c1, c2 = 0,0
        
        l = l1
        while l!=None:
            c1 += 1
            l = l.next
            
        l = l2
        while l!=None:
            c2 += 1
            l = l.next
            
        cmax, cmin = max(c1,c2), min(c1, c2)
        
        
        for i in range(cmax):
            if i<cmin:
                s = carry + l1.val+l2.val
                dummy.next = ListNode( s % 10)
                carry = s//10
                l1, l2 = l1.next, l2.next

            else:
                if c1 > c2:
                    s = l1.val+carry
                    dummy.next = ListNode(s % 10)
                    carry = s//10
                    l1 = l1.next
                else:
                    s = l2.val+carry
                    dummy.next = ListNode(s % 10)
                    carry = s//10
                    l2 = l2.next
                                
            dummy = dummy.next
        
        if carry:
            dummy.next = ListNode(carry)
            
        return head.next