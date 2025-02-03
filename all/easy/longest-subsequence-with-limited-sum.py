"""
2389. Longest Subsequence With Limited Sum
"""
from bisect import bisect_right
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        sums = [nums[0]] * len(nums)
        ans = []
        for index, num in enumerate(nums):
            if index == 0:
                continue
            sums[index] = sums[index - 1] + num
        for num in queries:
            index = find_less_than(sums, num)
            ans.append(index + 1)
        return ans


def find_less_than(arr: list, target):
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return [bisect_right(nums, q) for q in queries]


nums = [4, 5, 2, 1]
queries = [3, 10, 21]
print(Solution().answerQueries(nums, queries))
