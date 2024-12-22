"""
Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.
"""


class Solution2:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        for index, word in enumerate(s_list):
            s_list[index] = word[::-1]
        return ' '.join(s_list)


class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        start, end = 0, 0
        for i in range(len(s)):
            if s[i] == ' ' or i == len(s) - 1:
                end = i if i == len(s) - 1 else i -1
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                start = i + 1
        return ''.join(s)


s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))
