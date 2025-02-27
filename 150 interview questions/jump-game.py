"""
55. Jump Game
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

            if max_reach >= len(nums):
                return True
        return True


nums = [2, 3, 0, 0, 0, 0, 0]
print(Solution().canJump(nums))
