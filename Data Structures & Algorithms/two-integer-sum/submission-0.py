class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        imap = defaultdict(int)
        
        for i, n in enumerate(nums):
            if target - n in  imap:
                return [imap[target - n], i]
            imap[n] = i

        return (0,0)