"""
409. Longest Palindrome
Easy
Topics
Companies
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""
from collections import Counter


class Solution2:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = 0
        odd_found = False
        for value in counter.values():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                odd_found = True
        if odd_found:
            length += 1
        return length


class Solution:
    """
    another solution from others
    """
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0

        for char in s:
            if char in seen:
                seen.remove(char)
                length += 2
            else:
                seen.add(char)
        return length if not seen else length + 1


s = "abccccdd"
print(Solution().longestPalindrome(s))

