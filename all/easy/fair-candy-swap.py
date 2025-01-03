"""
888. Fair Candy Swap
"""
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_candies = sum(aliceSizes)
        bob_candies = sum(bobSizes)
        bob_set = set(bobSizes)
        diff = (alice_candies - bob_candies) // 2

        for candies in aliceSizes:
            y = candies - diff
            if y in bob_set:
                return [candies, y]


aliceSizes = [1, 1]
bobSizes = [2, 2]
print(Solution().fairCandySwap(aliceSizes, bobSizes))
