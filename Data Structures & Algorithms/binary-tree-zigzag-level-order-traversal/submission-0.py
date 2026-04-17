# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ret = []
        queue = deque()
        queue.append(root)


        while queue:
            level = []
            for _ in range(len(queue)):
                popped = queue.popleft()
                level.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            if len(ret) % 2 == 0:
                ret.append(level)
            else:
                ret.append(level[::-1])

        return ret
