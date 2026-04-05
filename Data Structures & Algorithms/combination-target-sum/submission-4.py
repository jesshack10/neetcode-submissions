class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []
        currSumNums = []

        def backtrack(i, currSum):
            if currSum > target or i >= len(nums):
                return
            if currSum == target:
                sums.append(currSumNums.copy())
                return
             
            currSumNums.append(nums[i])
            backtrack(i, currSum + nums[i])

            currSumNums.pop()
            backtrack(i + 1, currSum)

        backtrack(0,0)
        return sums

