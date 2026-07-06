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
                return [True, 0]
            
            left, right = helper(node.left), helper(node.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        
        return helper(root)[0]
    #     if not root:
    #         return True

    #     left = self.helper(root.left)
    #     right = self.helper(root.right)
    #     if abs(left-right) > 1:
    #         return False
        
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    # def helper(self, node):
    #     if not node:
    #         return 0

    #     left = self.helper(node.left)
    #     right = self.helper(node.right)

    #     return max(left, right) + 1


            