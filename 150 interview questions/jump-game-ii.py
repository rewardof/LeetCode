"""
45. Jump Game II
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        i = 0
        l = len(nums)
        if l == 1:
            return 0
        while i < l:
            if i + nums[i] >= l - 1:
                return jumps + 1
            max_index = -1
            max_value = -1
            for j in range(i + 1, nums[i] + i + 1):
                if max_value + max_index <= nums[j] + j:
                    max_index, max_value = j, nums[j]
            jumps += 1
            i = max_index
        return jumps

    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # Already at the last index

        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(n - 1):  # We stop at n-1 because the last jump lands us at the end
            farthest = max(farthest, i + nums[i])  # Find the farthest we can reach

            if i == current_end:  # If we reach the current boundary
                jumps += 1
                current_end = farthest  # Extend our boundary

                if current_end >= n - 1:  # If we can reach the end, break early
                    break

        return jumps


# nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
nums = [2, 3, 1, 1, 4]
print(Solution().jump2(nums))
