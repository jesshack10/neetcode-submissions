class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjlist = {i:[] for i in range(numCourses)}

        for c1, c2 in prerequisites:

            adjlist[c1] = [c2] + adjlist.get(c1,[])

        print(adjlist)
        #if a node is not as key in adjlist it means it does not have prereq

        seen = set()

        def dfs(node):
            if adjlist[node] == []:
                return True

            seen.add(node)

            for req  in adjlist[node]:
                if req in seen or not dfs(req):
                    return False

            seen.remove(node)
            adjlist[node] = []

            return True

        for i in range(numCourses - 1):
            if not dfs(i):
                return False

        return True

            