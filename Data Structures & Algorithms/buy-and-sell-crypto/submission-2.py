class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l= 0
        maxp = 0
        for r in range(1,len(prices)):
            if prices[l] < prices[r]:
                maxp = max(maxp, prices[r] - prices[l])
            else:
                l = r
        return maxp