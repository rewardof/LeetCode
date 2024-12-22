"""
804. Unique Morse Code Words
"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
            'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-",
            'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."
        }
        unique_trans = set()
        for word in words:
            trans = ''
            for char in word:
                trans += morse_dict[char]
            unique_trans.add(trans)

        return len(unique_trans)


words = ["gin", "zen", "gig", "msg"]
print(Solution().uniqueMorseRepresentations(words))