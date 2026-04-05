class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #define a dict
        numset = set()
        maxL = 0
        cnt = 0
        
        for num in nums:
            numset.add(num)

        for num in numset:
            prev = num - 1
            #init of sequence
            if prev not in numset:
                #Sequence is initialized from current num then
                prev = num
                while(prev in numset):
                    cnt = cnt + 1
                    prev = prev + 1
                maxL = max(maxL, cnt)
                cnt = 0
        return maxL