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

        oldtonew = {}
        oldtonew[node] = Node(node.val)
        queue = deque([node])

        while queue:
            popped = queue.popleft()
            for nei in popped.neighbors:
                if nei not in oldtonew:
                    oldtonew[nei] = Node(nei.val)
                    queue.append(nei)
                oldtonew[popped].neighbors.append(oldtonew[nei])
        
        return oldtonew[node]