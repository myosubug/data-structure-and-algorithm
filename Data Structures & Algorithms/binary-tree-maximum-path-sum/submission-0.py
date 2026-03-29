# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return
            left = self.getMax(node.left)
            right = self.getMax(node.right)
            res = max(res, node.val + left + right)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return res

    def getMax(self, node):
        if not node:
            return 0

        left = self.getMax(node.left)
        right = self.getMax(node.right)
        path = node.val + max(left, right)

        return max(0, path)