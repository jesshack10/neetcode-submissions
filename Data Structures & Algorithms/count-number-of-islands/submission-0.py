class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(grid, r, c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c]=="0" or (r,c) in visited:
                return 0

            #how to detect the island has finished

            visited.add((r,c))

            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)

            return 1

        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += dfs(grid, r, c)

        return islands

    
        