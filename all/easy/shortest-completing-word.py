"""
748. Shortest Completing Word
"""
from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Create a frequency counter for the license plate, considering only alphabetic characters
        license_freq = Counter(char.lower() for char in licensePlate if char.isalpha())
        # Initialize variables to track the shortest completing word
        shortest_word = None

        for word in words:
            word_freq = Counter(word)
            # Check if the word contains all characters in the license plate with at least the required frequency
            if all(word_freq[char] >= count for char, count in license_freq.items()):
                # Update shortest_word if the current word is shorter or if it's the first valid word
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word


licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(Solution().shortestCompletingWord(licensePlate, words))
