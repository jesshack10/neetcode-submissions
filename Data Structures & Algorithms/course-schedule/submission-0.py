class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjCourse = {i:[] for i in range(numCourses)}

        #Create the adj list for each course
        for crs, pr in prerequisites:
            if crs not in adjCourse:
                adjCourse[crs] = []
            adjCourse[crs].append(pr)

        visited = set()

        def dfs(courseIdx):
            if courseIdx in visited:
                return False

            #The list of prereq have been cleared
            if adjCourse[courseIdx] == []:
                return True
            
            visited.add(courseIdx)

            for req in adjCourse[courseIdx]:
                if not dfs(req):
                    return False
            
            visited.remove(courseIdx)
            adjCourse[courseIdx] = []

            return True
            
        for crs in range(numCourses - 1):
            if not dfs(crs):
                return False
            
        return True
        

