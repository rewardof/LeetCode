"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = start = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if end:
                    start = i + 1
                    break
            else:
                if not end:
                    end = i + 1

        return end - start


s = "a"
result = Solution().lengthOfLastWord(s)
print(result)