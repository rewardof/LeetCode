"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""
from collections import Counter
from typing import List


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        result = [0] * k
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        print(nums_dict)
        index = 0
        for num, occurance in nums_dict.items():
            if index < k:
                if index == 0:
                    result[index] = num
                else:
                    if occurance > nums_dict[result[index - 1]]:
                        result[index - 1], result[index] = num, result[index - 1]
                    else:
                        result[index] = num
            else:
                if occurance > nums_dict[result[index - 1]]:
                    result[index - 1], result[index] = num, result[index - 1]

            index = index + 1 if index < k else index
        print(result)


class Solution3:
    """
    easy solution
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n[0] for n in Counter(nums).most_common(n=k)]


class Solution:
    """
    easy solution
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        result = [0] * k
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        print(nums_dict)


nums = [2, 2, 1, 3, 3, 3]
k = 2
print(Solution().topKFrequent(nums, k))
