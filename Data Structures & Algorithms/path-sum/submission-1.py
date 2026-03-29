
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = [0]

        def helper(node):
            if node:
                pathSum[0] += node.val
                if not node.left and not node.right:

                    res = pathSum[0] == targetSum
                    pathSum[0] -= node.val
                    return res

                res = helper(node.left) or helper(node.right)
                pathSum[0] -= node.val
                return res
            else:
                return False

        
        return helper(root)