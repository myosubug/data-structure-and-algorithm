# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node:
                return True
            
            left = self.maxDepth(node.left)
            right = self.maxDepth(node.right)

            if abs(left-right) > 1:
                return False
            else:
                return helper(node.left) and helper(node.right)

        return helper(root)
    
    def maxDepth(self, node):
        if not node:
            return 0
        
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))