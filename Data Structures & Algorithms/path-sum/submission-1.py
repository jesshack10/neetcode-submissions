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

            #pathSum = currSum + node.val

            if ((currSum + node.val) == targetSum) and (not node.left) and (not node.right):
                return True
            
            if validSum(node.left, currSum + node.val):
                return True
            if validSum(node.right,currSum + node.val):
                return True

            return False

        return validSum(root, 0)
