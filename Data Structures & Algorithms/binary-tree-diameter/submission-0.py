# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            #Path trhough the current node
            res = max(res, left + right)
            #take the greatest pathof the two so far
            #i take into account ONLY the two nodes becaue if the greatest
            # was not the one passing though the node, the only valid paths are left and right
            # not the full tree left + node.val + right, that will be an invdalid path
            return 1 + max(left, right)

        dfs(root)
        return res