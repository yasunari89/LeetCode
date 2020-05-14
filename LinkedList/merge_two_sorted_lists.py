# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        if l1 and not l2:
            dummy.next = l1
        elif not l1 and l2:
            dummy.next = l2
        return dummy.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2
        elif not l1 and not l2:
            return None
        elif l1.val <= l2.val:
            node = ListNode(l1.val)
            node.next = self.mergeTwoLists2(l1.next, l2)
        elif l1.val > l2.val:
            node = ListNode(l2.val)
            node.next = self.mergeTwoLists2(l1, l2.next)
        return node