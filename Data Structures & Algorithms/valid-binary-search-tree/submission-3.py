# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, float('-inf'),root.val) and self.helper(root.right, root.val, float('inf'))

    def helper(self, node, left, right):
        if not node:
            return True
        
        if not (left < node.val < right):
            return False

        return self.helper(node.left, left, node.val) and self.helper(node.right, node.val, right)