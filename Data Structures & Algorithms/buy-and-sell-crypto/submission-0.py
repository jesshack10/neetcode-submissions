class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currmin = prices[0]
        for r in range(len(prices)):
            if prices[r] < currmin:
                currmin = prices[r]
            
            maxProfit = max(maxProfit, prices[r] - currmin)
        
        return maxProfit