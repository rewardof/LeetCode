"""
1385. Find the Distance Value Between Two Arrays
"""
import bisect
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for i in range(len(arr1)):
            index = bisect.bisect_left(arr2, arr1[i])
            before = arr2[index - 1] if index - 1 >= 0 else arr2[0]
            after = arr2[index] if index < len(arr2) else arr2[index - 1]
            if abs(arr1[i] - before) > d and abs(arr1[i] - after) > d:
                count += 1
        return count


class Solution2:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0

        for num in arr1:
            idx = bisect.bisect_left(arr2, num)

            left = abs(num - arr2[idx - 1]) if idx > 0 else float('inf')
            right = abs(num - arr2[idx]) if idx < len(arr2) else float('inf')

            if left > d and right > d:
                count += 1

        return count


arr1 = [2, 1, 100, 3]
arr2 = [-5, -2, 10, -3, 7]
d = 6
print(Solution().findTheDistanceValue(arr1, arr2, d))
