# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i, n in enumerate(inorder):
            inorder_map[n] = i
        
        def helper(pres, pree, ins, ine):
            if pres > pree:
                return None

            root = TreeNode(preorder[pres])
            mid = inorder_map[preorder[pres]]
            left_size = mid - ins

            root.left = helper(pres+1, pres+left_size, ins, mid-1)
            root.right = helper(pres+1+left_size, pree, mid+1, ine)

            return root

        return helper(0, len(preorder)-1, 0, len(inorder)-1)
