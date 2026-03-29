# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
         

        def helper(node, p, q):
            if not node or not p or not q:
                return 
            
            if min(p.val, q.val) > node.val:
                return helper(node.right, p, q)
            elif max(p.val, q.val) < node.val:
                return helper(node.left, p, q)
            else:
                return node

        return helper(root, p, q)