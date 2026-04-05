class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for index, val in enumerate(nums):
            num = nums[index]
            
            if nums[abs(num) - 1] < 0:
                return abs(num)
            
            nums[abs(num) - 1] *= -1