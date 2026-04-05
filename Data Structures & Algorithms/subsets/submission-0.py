class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cursubset, subsets = [], []

        def backtrack(i):
            if i >= len(nums):
                subsets.append(cursubset.copy())
                return
                
            cursubset.append(nums[i])
            backtrack(i + 1)

            cursubset.pop()
            backtrack(i + 1)

        backtrack(0)
        return subsets