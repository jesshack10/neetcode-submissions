class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        combination = []

        def dfs(i, currSum):
            if currSum == target:
                combinations.append(combination.copy())
                return

            if currSum > target or i >= len(nums):
                return

            #including the num index
            combination.append(nums[i])
            dfs(i, currSum + nums[i])
            combination.pop()
            dfs(i+1, currSum)

        dfs(0,0)

        return combinations