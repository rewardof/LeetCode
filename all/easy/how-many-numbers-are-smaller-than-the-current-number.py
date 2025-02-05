"""
1365. How Many Numbers Are Smaller Than the Current Number
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for index, num in enumerate(sorted(nums)):
            nums_dict[num] = nums_dict.get(num, index)
        ans = [0] * len(nums)
        for index, num in enumerate(nums):
            ans[index] = nums_dict[num]
        return ans


nums = [8, 1, 2, 2, 3]
print(Solution().smallerNumbersThanCurrent(nums))
