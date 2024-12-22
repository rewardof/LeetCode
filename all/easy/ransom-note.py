"""
383. Ransom Note
Easy
Topics
Companies
Given two strings ransomNote and magazine, return true
if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        as_dict = {}
        for char in magazine:
            as_dict[char] = as_dict.get(char, 0) + 1

        for char in ransomNote:
            if char in as_dict:
                as_dict[char] = as_dict[char] - 1
                if as_dict[char] == 0:
                    as_dict.pop(char)
            else:
                return False
        return True


ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))