# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []

        def helper(node):
            if not node:
                ret.append("N")
                return
            
            ret.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return ",".join(ret)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        split_data = data.split(",")
        self.i = 0

        def helper():
            if split_data[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(split_data[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()

            return node

        return helper()