class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        profit = 0
        
        while right < len(prices):
            tempProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                profit = max(profit, tempProfit)
            else:
                left = right
            right += 1
        return profit
            