class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        path = set()

        def dfs(i, j, index):
            if index == len(word):
                return True

            if (min(i, j) < 0 or
                i >= m or j >= n or
                word[index] != board[i][j] or
                (i, j) in path):
                return False
            
            path.add((i,j))                    # "I'm using this cell"
            res = (dfs(i-1, j, index+1) or
                dfs(i+1, j, index+1) or
                dfs(i, j-1, index+1) or
                dfs(i, j+1, index+1))
            path.remove((i,j))            # "done — put it back"

            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:          # possible start
                    if dfs(i, j, 0):
                        return True                  # found it!
        
        return False