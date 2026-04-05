class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            if nums[l] == val:
                nums[l] = nums[r - 1]
                r = r - 1
            else:
                l = l + 1

        return r