"""
884. Uncommon Words from Two Sentences
"""
from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts_s1 = Counter(s1.split(' '))
        counts_s2 = Counter(s2.split(' '))
        print(counts_s1)
        print(counts_s2)

        ans = []
        for word, count in counts_s1.items():
            if count == 1 and word not in counts_s2:
               ans.append(word)

        for word, count in counts_s2.items():
            if count == 1 and word not in counts_s1:
               ans.append(word)

        return ans


s1 = "this apple is sweet"
s2 = "this apple is sour"
print(Solution().uncommonFromSentences(s1, s2))

