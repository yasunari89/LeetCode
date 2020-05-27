from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        node1 = l1
        node2 = l2
        out = ListNode()
        first = out
        carry = 0
        node1, node2 = self.add_zero(node1, node2)
        while node1 != None:
            out.next = ListNode((node1.val+node2.val+carry)%10)
            carry = (node1.val + node2.val + carry) // 10
            node1 = node1.next
            node2 = node2.next
            out = out.next
        if carry > 0:
            out.next = ListNode(carry)
        return first.next
        
    def add_zero(self, node1, node2):
        counter1 = 0
        counter2 = 0
        first1 = node1
        first2 = node2
        while node1.next != None:
            counter1 += 1
            node1 = node1.next
        counter1 += 1
        while node2.next != None:
            counter2 += 1
            node2 = node2.next
        counter2 += 1
        if counter1 < counter2:
            for _ in range(counter2-counter1):
                node1.next = ListNode(0)
                node1 = node1.next
        if counter1 > counter2:
            for _ in range(counter1-counter2):
                node2.next = ListNode(0)
                node2 = node2.next
        return (first1, first2)
        
        