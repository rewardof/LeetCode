"""
209. Minimum Size Subarray Sum
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        window_sum = 0
        start = 0
        for i in range(len(nums)):
            window_sum += nums[i]
            if window_sum >= target:
                min_len = min(min_len, i - start + 1)
                while window_sum >= target:
                    window_sum -= nums[start]
                    start += 1
                min_len = min(min_len, i - start + 2)

        return 0 if min_len == float('inf') else min_len


target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(Solution().minSubArrayLen(target, nums))
