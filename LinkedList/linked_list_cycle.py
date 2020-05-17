# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
    def hasCycle2(self, head: ListNode) -> bool:
        hash_table = {}
        curr = head
        while curr:
            if curr in hash_table:
                return True
            hash_table[curr] = True
            curr = curr.next
        return False