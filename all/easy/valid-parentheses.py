from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        chars = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for char in s:
            if char in chars:
                stack.append(char)
            else:
                if not stack and chars[stack.pop()] != char:
                    return False
        return not stack


s = "[]({}[])[(())]{}"
a = Solution().isValid(s)
print(a)
