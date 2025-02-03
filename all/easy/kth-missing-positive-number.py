"""
1539. Kth Missing Positive Number
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 0
        count_missed = 0
        for num in arr:
            count_missed += num - last - 1
            if count_missed >= k:
                return num + k - count_missed - 1
            last = num
        return k - count_missed + num


arr = [1, 2, 3, 4]
k = 2
print(Solution().findKthPositive(arr, k))
