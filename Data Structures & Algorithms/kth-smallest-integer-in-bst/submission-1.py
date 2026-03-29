# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder(root)[k-1]
    

    def inorder(self, node):
        ret = []
        def traverse(node):
            if node:
                traverse(node.left)
                ret.append(node.val)
                traverse(node.right)

        traverse(node)

        return ret
                