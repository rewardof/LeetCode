"""
2089. Find Target Indices After Sorting Array
"""
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for index, num in enumerate(nums):
            if num == target:
                ans.append(index)
        return ans
