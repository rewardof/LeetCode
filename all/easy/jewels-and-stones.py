"""
771. Jewels and Stones
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        jewels_count = 0
        for stone in stones:
            if stone in jewels_set:
                jewels_count += 1
        return jewels_count


jewels = "aA"
stones = "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))



