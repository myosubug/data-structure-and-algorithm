# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.helper(root, p, q)


    def helper(self, node, p, q):
        if not p or not q or not node:
            return None

        if min(p.val, q.val) > node.val:
            return self.helper(node.right, p, q)
        elif max(p.val, q.val) < node.val:
            return self.helper(node.left, p, q)
        else:
            return node