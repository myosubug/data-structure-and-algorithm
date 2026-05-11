# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        collector = []

        def helper(node):
            if node:
                if node.left:
                    helper(node.left)
                collector.append(node.val)
                if node.right:
                    helper(node.right)

            return
        helper(root)

        return collector[k-1]
        