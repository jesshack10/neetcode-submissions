class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combinations = []

        def dfs(i, currSum, combination):
            if currSum == target:
                combinations.append(combination.copy())
                return

            if currSum > target or i >= len(nums):
                return

            #including the num index
            combination.append(nums[i])
            dfs(i, currSum + nums[i], combination)
            combination.pop()
            dfs(i+1, currSum, combination)

        dfs(0, 0, [])

        return combinations