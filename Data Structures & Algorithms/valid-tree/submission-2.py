class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        if not edges:
            return True
        visited = set()
        adj = {}

        for src, dst in edges:
            adj[src] = [dst] + adj.get(src, [])
            adj[dst] = [src] + adj.get(dst, [])

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for n in adj[node]:
                if n == prev:
                    continue
                if not dfs(n, node):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n

        