"""
496. Next Greater Element I
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_element = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater_element[smaller] = num
            stack.append(num)

        while stack:
            no_greater = stack.pop()
            next_greater_element[no_greater] = -1
        return [next_greater_element[num] for num in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))
