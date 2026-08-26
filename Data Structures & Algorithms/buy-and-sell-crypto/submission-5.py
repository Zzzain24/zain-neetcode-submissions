class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit, b, s = 0, 0, 1
        while s < len(prices):
            profit = prices[s] - prices[b]
            mProfit = max(mProfit, profit)
            if prices[b] < prices[s]:
                s += 1
            else:
                b = s
                s += 1
        return mProfit
        