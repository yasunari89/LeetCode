# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        dummy = ListNode()
        dummy.next = head
        p = head
        counter = length - n
        if counter > 0:
            for _ in range(counter-1):
                p = p.next
            p.next = p.next.next
        else:
            head = head.next
        return head