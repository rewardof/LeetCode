"""
Given two integer arrays nums1 and nums2, return an array of their
intersection
. Each element in the result must be unique and you may return the result in any order.
"""
from typing import List


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        result = []
        for index, value in enumerate(nums1):
            nums1_dict[value] = index

        for num in nums2:
            if num in nums1_dict:
                result.append(num)
                nums1_dict.pop(num)

        return result


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)


class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        n1 = len(nums1)
        n2 = len(nums2)

        intersection = set()

        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                intersection.add(nums1[i])
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return list(intersection)


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersection(nums1, nums2))
