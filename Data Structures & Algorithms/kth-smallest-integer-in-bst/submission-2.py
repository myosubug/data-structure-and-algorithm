# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = []
        self.inOrderHelper(root, ret)

        return ret[k-1]

    def inOrderHelper(self, node, ret):
        if node:
            if node.left:
                self.inOrderHelper(node.left, ret)
            ret.append(node.val)
            if node.right:
                self.inOrderHelper(node.right, ret)
        
        return ret