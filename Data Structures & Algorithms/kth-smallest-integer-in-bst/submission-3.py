# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        col = []

        def helper(node, collect):
            if node:
                if node.left:
                    helper(node.left, collect)
                
                collect.append(node.val)
                
                if node.right:
                    helper(node.right, collect)
        
        helper(root, col)

        return col[k-1]
