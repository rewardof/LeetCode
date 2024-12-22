"""
205. Isomorphic Strings
Easy
Topics
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters. No two characters may map to the
 same character, but a character may map to itself.

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_to_t = {}
        t_to_s = {}

        for char1, char2 in zip(t, s):
            if char1 in t_to_s:
                if t_to_s[char1] != char2:
                    return False
            else:
                t_to_s[char1] = char2

            if char2 in s_to_t:
                if s_to_t[char2] != char1:
                    return False
            else:
                s_to_t[char2] = char1
        return True