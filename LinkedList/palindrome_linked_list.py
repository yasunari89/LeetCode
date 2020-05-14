# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next
        curr = head
        count = int((counter-1)/2) if counter%2 else int(counter/2)
        memo = []
        for _ in range(count):
            memo.append(curr.val)
            curr = curr.next
        curr = curr.next if counter%2 else curr
        for i in range(count):
            if curr.val != memo[-i-1]:
                return False
            curr = curr.next
        return True
        