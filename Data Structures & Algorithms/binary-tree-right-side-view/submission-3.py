# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        ret = []
        collection = []

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
            collection.append(level)

        for l in collection:
            ret.append(l[-1])

        return ret