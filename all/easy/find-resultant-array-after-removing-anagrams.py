"""
2273. Find Resultant Array After Removing Anagrams
"""
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev_sorted = ""
        for word in words:
            current_sorted = "".join(sorted(word))
            if prev_sorted != current_sorted:
                result.append(current_sorted)
                prev_sorted = current_sorted
        return result


words = ["abba", "baba", "bbaa", "cd", "cd"]
print(Solution().removeAnagrams(words))
