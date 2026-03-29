# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # bottom up
        def helper(node):
            if not node:
                return [True, 0]

            left, right = helper(node.left), helper(node.right)
            balanced = False
            if left[0] and right[0] and abs(left[1]-right[1]) <= 1:
                balanced = True
            
            return [balanced, 1 + max(left[1],right[1])]

        return helper(root)[0]

    # top down
    #     def helper(node):
    #         if not node:
    #             return True
            
    #         left = self.maxDepth(node.left)
    #         right = self.maxDepth(node.right)

    #         if abs(left-right) > 1:
    #             return False
    #         else:
    #             return helper(node.left) and helper(node.right)

    #     return helper(root)
    
    # def maxDepth(self, node):
    #     if not node:
    #         return 0
        
    #     return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))