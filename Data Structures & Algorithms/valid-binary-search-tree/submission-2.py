# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.check(root.left, float('-inf'), root.val) and self.check(root.right, root.val, float('inf'))
    

    def check(self, node, miv, mav):
        if not node:
            return True
        
        if not(miv < node.val < mav):
            return False

        return self.check(node.left, miv, node.val) and self.check(node.right, node.val, mav)
