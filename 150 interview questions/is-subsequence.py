"""
392. Is Subsequence
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        last_index = 0
        for i in range(len(s)):
            equal = True
            if last_index >= len(t):
                return False
            while equal and last_index < len(t):
                if s[i] == t[last_index]:
                    equal = False
                last_index += 1
        return True

    def isSubsequence2(self, s: str, t: str) -> bool:
        if not s:
            return True
        last_index = 0
        for c in t:
            if last_index >= len(s):
                break
            if s[last_index] == c:
                last_index += 1
            else:
                continue
        return last_index == len(s)






s = "b"
t = "abs"
print(Solution().isSubsequence2(s, t))