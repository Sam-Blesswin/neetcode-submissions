class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        itr=0
        for i,p in enumerate(prices):
            profit = max(profit, p - prices[itr])
            if p<prices[itr]:
                itr = i
        return profit
