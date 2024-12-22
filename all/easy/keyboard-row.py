"""
500. Keyboard Row
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        result = []
        for word in words:
            word_copy = word.lower()
            searching = ''
            if word_copy[0] in first_row:
                searching = first_row

            elif word_copy[0] in second_row:
                searching = second_row

            elif word_copy[0] in third_row:
                searching = third_row
            count = 0
            for char in word_copy:
                if char in searching:
                    count += 1
            if len(word) == count:
                result.append(word)
        return result

    def findWords2(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        result = []
        for word in words:
            word_lower = set(word.lower())
            if word_lower.issubset(first_row) or word_lower.issubset(second_row) or word_lower.issubset(third_row):
                result.append(word)

        return result


words = ["Hello", "Alaska", "Dad", "Peace"]
print(Solution().findWords(words))
