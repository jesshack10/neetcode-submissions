# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #i will use bfs

        #traverse the tree
        #as i am traversing the tree, save the las value in the queue at that time
        #output those save values in an array

        if not root:
            return []

        q = deque()
        arr = []

        q.append(root)

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

                if i == 0:
                    arr.append(node.val)

        return arr            

            
