# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        a = []
        b = []
        self.serialize(root, a)
        self.serialize(subRoot, b)

        a_s = "".join(a)
        b_s = "".join(b)

        return True if b_s in a_s else False

    def serialize(self, node, arr):
        if not node:
            arr.append("N")
            return
        
        arr.append(str(node.val))
        self.serialize(node.left, arr)
        self.serialize(node.right, arr)

        return