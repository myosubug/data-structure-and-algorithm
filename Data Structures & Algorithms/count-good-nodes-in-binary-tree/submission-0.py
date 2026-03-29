# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, maximum):
            if not node:
                return 0

            res = 1 if node.val >= maximum else 0
            maximum = max(maximum, node.val)
            res += helper(node.left, maximum)
            res += helper(node.right, maximum)

            return res

        return helper(root, root.val)