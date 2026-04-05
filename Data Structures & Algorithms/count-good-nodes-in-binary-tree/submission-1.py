# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, cm):
            if not node:
                return
            #print(node.val)
            currm = max(node.val,cm)
            
            if node.val >= cm:
                nonlocal res
                res += 1
            
            dfs(node.left, currm)
            dfs(node.right, currm)

        dfs(root, root.val)
        return res