"""
122. Best Time to Buy and Sell Stock II
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit


prices = [1, 2, 3, 4, 5]
print(Solution().maxProfit(prices))
