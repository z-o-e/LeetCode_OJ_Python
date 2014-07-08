# Definition for singly-linked list.
# class ListNode:
#     def __init__(self,x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head==None or m==n:
            return head
            
        dummy = ListNode(-1)
        dummy.next  = head
        
        p =dummy
        
        for i in range(n+1):
            if i==m-1:
                ppm = p
                
            elif i==m:
                pm = p
            
            elif i==n:
                pn = p
                
            tmp = p.next
            if i>m and i<=n:
                p.next = pre
            pre = p
            p = tmp
            
        ppm.next = pn
        pm.next = p
        
        return dummy.next