"""
238. Product of Array Except Self
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        ans = [1] * n
        prefix[0] = 1
        suffix[n - 1] = 1
        for i in range(1, n):
            j = n - 1 - i
            prefix[i] = prefix[i - 1] * nums[i - 1]  # Multiply by previous element
            suffix[j] = suffix[j + 1] * nums[j + 1]  # Multi
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        return ans

nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))



"""
[a1, a2, a3, a4, a5]
[1, a2, a2 * a3, a2 * a3 * a4, a2 * a3 * a4 * a5]
[a4 * a3 * a2 * a1, a4 * a3 * a2, a4 * a3, a4, 1]
[a4 * a3 * a2 * a1, a2 * a3 * a4 * a3 * a2]

[1, a1, a1 * a2, a1 * a2 * a3, a1 * a2 * a3 * a4]
[a2 * a3 * a4 * a5, a3 * a4 * a5, a4 * a5, a5, 1]

[a2 * a3 * a4 * a5, a1 * a3 * a4 * a5, a1 * a2 * a4 * a5, a1 * a2 * a3 * a4 * a5]

"""