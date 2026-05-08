# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1

        def calc_depth(root, currdepth):
            nonlocal depth
            if not root:
                return
            depth = max(depth, currdepth)
            
            calc_depth(root.left, currdepth + 1)
            calc_depth(root.right, currdepth + 1)

        calc_depth(root, 1)

        return depth
