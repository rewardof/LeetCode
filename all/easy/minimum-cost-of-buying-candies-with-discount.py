"""
2144. Minimum Cost of Buying Candies With Discount
"""
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        min_cost = 0
        for index, c in enumerate(cost):
            if (index + 1) % 3 != 0:
                min_cost += c
        return min_cost

    def minimumCost2(self, cost: List[int]) -> int:
        return sum(i for i, c in enumerate(sorted(cost, reverse=True)) if (i + 1) % 3)


cost = [1, 2, 3]
print(Solution().minimumCost(cost))
