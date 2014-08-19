# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        dummy = head = ListNode(-1)
       
        while l1!=None or l2!=None:
            if l2==None:
                head.next = l1
                break
            elif l1==None:
                head.next = l2
                break
                
            else:
                if l1.val<l2.val:
                    head.next = l1
                    l1 = l1.next
                    
                else:
                    head.next = l2
                    l2 = l2.next
            
            head = head.next
            
        return dummy.next