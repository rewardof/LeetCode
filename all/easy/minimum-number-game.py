"""
2974. Minimum Number Game
"""
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        arr = []
        while i < len(nums):
            arr.append(nums[i + 1])
            arr.append(nums[i])
            i += 2
        return arr

    def numberGame2(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(0, len(nums), 2):  # Iterate in steps of 2
            arr.append(nums[i + 1])
            arr.append(nums[i])
        return arr


nums = [5, 4, 2, 3]
print(Solution().numberGame2(nums))
