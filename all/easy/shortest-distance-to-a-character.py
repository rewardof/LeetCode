"""
821. Shortest Distance to a Character
Easy
Topics
Companies
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length
and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
"""
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [float('inf')] * n
        prev = float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = abs(prev - i)

        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], abs(prev - i))
        return result


s = "aaba"
c = "b"

print(Solution().shortestToChar(s, c))
