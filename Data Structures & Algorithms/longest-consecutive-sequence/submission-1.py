class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_sequence = 0

        for num in nums:
            #start of a pattern
            if (num - 1) not in seen:
                currSeqLen = 0
                currnum = num
                while currnum in seen:
                    currnum += 1
                    currSeqLen += 1

                longest_sequence = max(longest_sequence, currSeqLen)

        
        return longest_sequence
