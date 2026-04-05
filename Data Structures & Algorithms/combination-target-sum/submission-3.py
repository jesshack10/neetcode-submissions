class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        currNums, combinations = [], []

        def dfs(i, curSum):
            if curSum > target or i >= len(nums):
                return
            if curSum == target:
                combinations.append(currNums.copy())
                return

            currNums.append(nums[i])
            dfs(i, curSum + nums[i])

            currNums.pop()
            dfs(i+1,  curSum)

        dfs(0,0)
        return combinations