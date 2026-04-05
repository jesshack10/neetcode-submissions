class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k: return False

        window = set()
        l = 0
        for i in range(k):
            if nums[i] in window:
                return True
            window.add(nums[i])

        for r in range(k, len(nums)):
            if nums[r] in window:
                return True
            window.remove(nums[l])
            l = l + 1
            window.add(nums[r])

        return False

        