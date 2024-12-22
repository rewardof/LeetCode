"""
This problem is a classic example of finding the maximum profit from stock prices, often solved using a **single pass** approach. Here's a hint to guide you:

### Key Idea:
- To maximize profit, you want to **buy at the lowest price** seen so far and **sell at the highest price** afterwards.
- Keep track of the **minimum price encountered so far** as you traverse the list and calculate the potential profit at each step.

### Approach:
1. **Initialize** two variables:
   - `min_price` to a very large number (to track the lowest price encountered so far).
   - `max_profit` to 0 (to track the maximum profit found).

2. **Iterate** through the prices:
   - If the current price is less than `min_price`, update `min_price` to the current price.
   - Otherwise, calculate the profit as `current_price - min_price` and update `max_profit` if the profit is greater than the current `max_profit`.

3. The `max_profit` at the end will be your result.

### Pseudocode:
```python
min_price = float('inf')  # Start with a very high price
max_profit = 0            # Initial max profit

for price in prices:
    if price < min_price:
        min_price = price  # Update min_price if we find a lower price
    else:
        profit = price - min_price  # Calculate profit with the current price
        max_profit = max(max_profit, profit)  # Update max profit if this is higher

return max_profit
```

This ensures that you find the optimal buy and sell days while maintaining **O(n)** time complexity and **O(1)** space complexity.

Would you like to see a full implementation?
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        profit = 0
        if length <= 2:
            profit = prices[1] - prices[0]
        for i in range(length):
            for j in range(i + 1, length):
                new_profit = prices[j] - prices[i]
                if profit < new_profit:
                    profit = new_profit

        return profit if profit > 0 else 0


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 1000000000000000000
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(profit, max_profit)
        return max_profit


prices = [7, 1, 5, 3, 6, 4]

result = Solution2().maxProfit(prices)
