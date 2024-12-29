"""
819. Most Common Word
"""
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_dict = {}
        paragraph = [word for word in re.split(r'\W+', paragraph) if word]
        for word in paragraph:
            word = ''.join(char.lower() for char in word if char.isalpha())
            paragraph_dict[word.lower()] = paragraph_dict.get(word, 0) + 1
        banned = set(banned)
        max_occurance = 0
        most_frequent = None
        for word, count in paragraph_dict.items():
            if word not in banned:
                if count > max_occurance:
                    max_occurance = count
                    most_frequent = word

        return most_frequent


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))

