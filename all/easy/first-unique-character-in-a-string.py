"""
387. First Unique Character in a String
Easy
Topics
Companies
Given a string s, find the first non-repeating character
in it and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar2(self, s: str) -> int:
        repeated_one = {}
        repeated_more = {}
        for index, char in enumerate(s):
            if char not in repeated_one and char not in repeated_more:
                repeated_one[char] = index
            else:
                repeated_one.pop(char, None)
                repeated_more[char] = repeated_more.get(char, 1) + 1
        for char, index in repeated_one.items():
            return index
        return -1

    def firstUniqChar(self, s: str) -> int:
        as_dict = {}
        for index, char in enumerate(s):
            if char in as_dict:
                as_dict[char] = None
            else:
                as_dict[char] = index

        for char, index in as_dict.items():
            if index is not None:
                return index
        return -1


class Solution2:
    """
    best solution
    """

    def firstUniqChar(self, s: str) -> int:
        ans = 10 ** 5

        for letter in 'qwertyuiopasdfghjklzxcvbnm':
            if s.find(letter) == s.rfind(letter) != -1:
                ans = min(s.find(letter), ans)

        if ans != 10 ** 5:
            return ans

        return -1


s = "leetcode"
print(Solution().firstUniqChar(s))
