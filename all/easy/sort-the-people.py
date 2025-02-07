"""
2418. Sort the People
"""
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        as_dict = dict(zip(heights, names))
        heights.sort(reverse=True)
        ans = []
        for height in heights:
            ans.append(as_dict[height])
        return ans

    def sortPeople2(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(Solution().sortPeople2(names, heights))
