# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # lists in Python are mutable objects When you pass a list to a function, 
        # you can modify its contents and those changes 
        # will be visible outside the function.
        ret = [root.val]

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            ret[0] = max(ret[0], node.val + left + right)

            return node.val + max(left, right)

        dfs(root)

        return ret[0]