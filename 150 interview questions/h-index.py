"""
274. H-Index
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i, num in enumerate(citations):
            if not (i + 1 > num):
                h_index = max(h_index, i + 1)
        return h_index

    def hIndex2(self, citations: List[int]) -> int:
        l = len(citations)
        papers_counts = [0] * (l + 1)
        for citation in citations:
            papers_counts[min(l, citation)] += 1
        num_papers = 0
        for i in range(l, -1, -1):
            num_papers += papers_counts[i]
            if num_papers >= i:
                return i


citations = [3, 0, 6, 1, 5]
print(Solution().hIndex2(citations))

