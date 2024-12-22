"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        n1, n2 = 1, 2
        for _ in range(3, n + 1):
            n1, n2 = n2, n1 + n2
        return n2


n = 5
result = Solution().climbStairs(n)
print(result)

"""
This problem is a classic example of a **dynamic programming** question. Here's a structured hint to approach the solution:

---

### Key Observations:
1. **Recursive Nature**:
   - If you are on step \( n \), you could have arrived there from \( n-1 \) (by taking 1 step) or \( n-2 \) (by taking 2 steps).
   - The total number of ways to reach \( n \) is therefore the sum of the ways to reach \( n-1 \) and \( n-2 \).

   **Formula**:
   \[
   f(n) = f(n-1) + f(n-2)
   \]

2. **Base Cases**:
   - \( f(1) = 1 \): There is only one way to climb one step.
   - \( f(2) = 2 \): You can climb two steps in two ways: \( 1+1 \) or \( 2 \).

---

### Hint for Solution:
1. Start with the base cases \( f(1) = 1 \) and \( f(2) = 2 \).
2. Use either:
   - **Recursion with Memoization**: Cache results of subproblems to avoid redundant calculations.
   - **Iterative Dynamic Programming**: Use a loop to calculate \( f(n) \) step by step, storing only the last two results to save space.

---

### Example for \( n = 5 \):
- \( f(3) = f(2) + f(1) = 2 + 1 = 3 \)
- \( f(4) = f(3) + f(2) = 3 + 2 = 5 \)
- \( f(5) = f(4) + f(3) = 5 + 3 = 8 \)

So there are 8 ways to climb 5 steps.
"""
