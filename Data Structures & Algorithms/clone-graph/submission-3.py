"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {node: Node(node.val)}
        queue = deque()
        queue.append(node)

        while queue:
            popped = queue.popleft()
            for nei in popped.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    queue.append(nei)
                oldToNew[popped].neighbors.append(oldToNew[nei])

        return oldToNew[node]