from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        queue = [[root]]
        ans = []
        while queue != [[]]:
            nodes = queue.pop(0)
            vals = [node.val for node in nodes if node != None]
            ans.append(vals)
            node_list = []
            for node in nodes:
                if node.left != None:
                    node_list.append(node.left)
                if node.right != None:
                    node_list.append(node.right)
            queue.append(node_list)
        return ans
            
            
        