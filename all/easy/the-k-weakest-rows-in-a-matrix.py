"""
1337. The K Weakest Rows in a Matrix
"""
from collections import Counter
from typing import List


class Solution:
    """
    this is the best solution, idea is mine)
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        for index, i in enumerate(mat):
            first = self.firstZeroIndex(i)
            result.append((first, index))

        result.sort()

        return [result[j][1] for j in range(k)]

    def firstZeroIndex(self, row):
        low, high = 0, len(row) - 1
        result = len(row)  # Default to len(row) if no zero is found
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == 0:
                result = mid  # Update result and search left for earlier zero
                high = mid - 1
            else:
                low = mid + 1
        return result


class Solution2:
    """
    direct solution
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        for index, i in enumerate(mat):
            counts = Counter(i)
            result.append((counts[1], index))
        result.sort()
        ans = []
        for j in range(k):
            ans.append(result[j][1])
        return ans


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

k = 3
print(Solution().kWeakestRows(mat, k))
