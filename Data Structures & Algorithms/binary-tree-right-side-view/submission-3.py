# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        q = deque()
        if root:
            q.append(root)

        while q:
            qLen = len(q)
            for i in range(qLen):
                currnode = q.popleft()
                if currnode.left:
                    q.append(currnode.left)
                if currnode.right:
                    q.append(currnode.right)
                #The last element is the rightest value in the tree
                if i == (qLen - 1):
                    res.append(currnode.val)
        
        return res

