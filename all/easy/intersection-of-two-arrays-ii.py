"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.
"""
from typing import List


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        for num in nums1:
            if num not in nums1_dict:
                nums1_dict[num] = 1
            else:
                nums1_dict[num] += 1

        result = list()
        for num in nums2:
            if num in nums1_dict and nums1_dict[num] > 0:
                result.append(num)
                nums1_dict[num] -= 1
        return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersect(nums1, nums2))
