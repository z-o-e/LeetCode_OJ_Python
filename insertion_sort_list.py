# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        pre = cur = dummy = ListNode(0)
        dummy.next = head

        while cur.next:
            # reset only when next node val is less than current insertion node
            if pre.next.val > cur.next.val:
                pre = dummy

            while pre.next.val < cur.next.val:
                pre = pre.next

            if pre != cur:
                node = cur.next
                cur.next = node.next
                node.next = pre.next
                pre.next = node
            else:
                cur = cur.next

        return dummy.next
