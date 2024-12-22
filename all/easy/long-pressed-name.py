"""
925. Long Pressed Name
Easy
Topics
Companies
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed,
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for m, char in enumerate(name):
            if name[m] != name[i]:
                j = 0
                for n, ch in enumerate(typed):
                    if typed[n] != typed[j]:
                        if char == char and len(typed[j:n]) % len(name[i:m]) % 0:
                            pass
                        else:
                            return False
                        j = n
                i = m
        return True

    def isLongPressedName2(self, name: str, typed: str) -> bool:
        i = j = 0
        for m, char in enumerate(name):
            for n, ch in enumerate(typed):
                if m == n:
                    continue

        return True


name = "alex"
typed = "aaleex"
print(typed[2:3])
print(Solution().isLongPressedName(name, typed))
