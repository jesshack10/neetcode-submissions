class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqmap = {}

        for i in range(numCourses):
            #add an empty array when no prereq for course is needed
            prereqmap[i] = []

        for course, prereq in prerequisites:
            prereqmap[course].append(prereq)
        
        visiting = set()
        completed = set()
        res = []
        
        def dfs(courseIdx):
            if courseIdx in visiting:
                return False

            if courseIdx in completed:
                return True

            visiting.add(courseIdx)

            for prereq in prereqmap[courseIdx]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(courseIdx)
            completed.add(courseIdx)
            
            res.append(courseIdx)

            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return res

