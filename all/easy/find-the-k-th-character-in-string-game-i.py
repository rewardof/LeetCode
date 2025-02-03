"""
3304. Find the K-th Character in String Game I
"""


class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            generated = ''
            for char in word:
                generated += chr(ord(char) + 1)
            word += generated

        return word[k-1]


print(Solution().kthCharacter(k=10))
