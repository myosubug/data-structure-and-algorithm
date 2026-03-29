# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            max_diameter[-1] = max(max_diameter[-1], left + right)

            return 1 + max(helper(node.left), helper(node.right))
        
        helper(root)
    
        return max_diameter[-1]