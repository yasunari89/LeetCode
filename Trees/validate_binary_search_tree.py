# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBSTRecursion(self, root: TreeNode) -> bool:
        def helper(node, minvalue=float('-inf'), maxvalue=float('inf')):
            if not node:
                return True
            value = node.val
            if value <= minvalue or value >= maxvalue:
                return False
            if not helper(node.left, minvalue, value):
                return False
            if not helper(node.right, value, maxvalue):
                return False
            return True
        return helper(root)
    
    def isValidBSTIteration(self, root: TreeNode) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, minvalue, maxvalue = stack.pop()
            if not node:
                continue
            value = node.val
            if value <= minvalue or value >= maxvalue:
                return False
            stack.append((node.left, minvalue, value))
            stack.append((node.right, value, maxvalue))
        return True