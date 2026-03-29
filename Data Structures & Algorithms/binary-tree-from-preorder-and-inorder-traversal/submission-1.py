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

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            root_value = preorder[pre_start]
            root = TreeNode(root_value)
            
            mid = inorder_map[root_value]
            left_size = mid - in_start

            root.left = helper(
                pre_start + 1,
                pre_start + left_size,
                in_start,
                mid-1
            )

            root.right = helper(
                pre_start + 1 + left_size,
                pre_end,
                mid + 1,
                in_end
            )

            return root
        
        return helper(0, len(preorder)-1, 0, len(inorder)-1)
        
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root