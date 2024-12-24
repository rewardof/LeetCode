"""
389. Find the Difference
Easy
Topics
Companies
You are given two strings s and t.

String t is generated by random shuffling
string s and then add one more letter at a random position.

Return the letter that was added to t.
"""
from collections import defaultdict


class Solution:
    def findTheDifference2(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1

        for char in t:
            if char in s_dict and s_dict[char] > 0:
                s_dict[char] -= 1
            else:
                return char

    def findTheDifference3(self, s: str, t: str) -> str:
        sum1 = 0
        for char in s:
            sum1 += ord(char)
        sum2 = 0
        for char in t:
            sum2 += ord(char)

        return chr(sum2 - sum1)

    def findTheDifference4(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s + t:
            result ^= ord(char)

        return chr(result)

s = "a"
t = "aa"
print(Solution().findTheDifference(s, t))