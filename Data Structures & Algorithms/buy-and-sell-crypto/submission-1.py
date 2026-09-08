class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j=0
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, prices[i] - prices[j])
            if prices[i] < prices[j]:
                j=i
        return profit
            
        