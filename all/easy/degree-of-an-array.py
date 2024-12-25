"""
697. Degree of an Array
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def findShortestSubArray2(self, nums: List[int]) -> int:
        counter = Counter(nums)
        degree = 0
        result = set()
        for key, value in counter.items():
            if value > degree:
                degree = value
                result = {key}
            elif value == degree:
                result.add(key)

        ans = defaultdict(list)
        for index, num in enumerate(nums):
            if num in result:
                ans[num].append(index)

        min_len = pow(10, 10)
        for value in ans.values():
            l = value[-1] - value[0]
            if l < min_len:
                min_len = l
        return min_len + 1

    def findShortestSubArray(self, nums: List[int]) -> int:
        first_occurance = {}
        las_occurance = {}
        frequency = {}
        degree = 0
        min_len = len(nums)
        for i, num in enumerate(nums):
            if num not in first_occurance:
                first_occurance[num] = i
            las_occurance[num] = i
            frequency[num] = frequency.get(num, 0) + 1
            degree = max(degree, frequency[num])

        for num, occurance in frequency.items():
            if occurance == degree:
                min_len = min(min_len, las_occurance[num] - first_occurance[num])

        return min_len + 1


nums = [1, 2, 2, 3, 1]
print(Solution().findShortestSubArray(nums))
