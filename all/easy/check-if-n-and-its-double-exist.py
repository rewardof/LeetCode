from collections import Counter
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        for num in arr:
            pair = num * 2
            if pair in counts:
                if pair != num or pair == num and counts[pair] > 1:
                    return True
        return False


arr = [-20, 8, -6, -14, 0, -19, 14, 4]
print(Solution().checkIfExist(arr))
