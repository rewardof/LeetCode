"""
Given a string s, return true if the s can be palindrome
after deleting at most one character from it.
"""


class Solution2:
    """
    bu meni yechimim, ammo, u xato ekan, deyarli to'g'ri ekan))
    """

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        skipped = False
        while i < j:
            if s[i] != s[j] and not skipped:
                if s[i + 1] == s[j]:
                    i += 2
                    skipped = True
                    continue
                elif s[i] == s[j - 1]:
                    j -= 2
                    skipped = True
                    continue
                return False

            i += 1
            j -= 1
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return is_palindrome(i + 1, j) or is_palindrome(i, j - 1)
            i += 1
            j -= 1
        return True


s = "eeccccbebaeeabebcccee"
print(Solution().validPalindrome(s))
