class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [ [] for _ in range(len(nums) + 1)]
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for num, f in freq.items():
            bucket[f].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res