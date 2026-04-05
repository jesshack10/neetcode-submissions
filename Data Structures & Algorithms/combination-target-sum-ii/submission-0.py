class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        sums = []
        currCandidates = []
        candidates.sort()

        def dfs(i, currSum):

            if currSum == target:
                sums.append(currCandidates.copy())
                return

            if currSum > target or i >= len(candidates):
                return
            

            currCandidates.append(candidates[i])
            dfs(i + 1, currSum + candidates[i])

            #avoidng dup nums
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1

            currCandidates.pop()
            dfs(i + 1 , currSum)

        dfs(0, 0)
        print(sums)

        return sums
