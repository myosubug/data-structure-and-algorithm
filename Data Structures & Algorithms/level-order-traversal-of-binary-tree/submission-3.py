# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        

        ret = []
        nodes = deque([root])

        while nodes:
            level = []
            for _ in range(len(nodes)):
                popped = nodes.popleft()
                level.append(popped.val)
                if popped.left:
                    nodes.append(popped.left)
                if popped.right:
                    nodes.append(popped.right)
            ret.append(level)

        return ret
