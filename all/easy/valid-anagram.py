"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for value in s:
            s_dict[value] = s_dict.get(value, 0) + 1
        for value in t:
            if value in s_dict and s_dict[value] > 0:
                s_dict[value] -= 1
                if s_dict[value] == 0:
                    s_dict.pop(value)
            else:
                return False
        return True if len(s_dict) == 0 else False


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
