"""
917. Reverse Only Letters
Easy
Topics
Companies
Hint
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
                continue
            if not s[j].isalpha():
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)


s = "ab-cd"
print(Solution().reverseOnlyLetters(s))
