# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def validSum(node, currSum):
            if not node:
                return False

            pathSum = currSum + node.val

            if (pathSum == targetSum) and (not node.left) and (not node.right):
                return True
            
            if validSum(node.left, pathSum):
                return True
            if validSum(node.right,pathSum):
                return True

            return False

        return validSum(root, 0)
