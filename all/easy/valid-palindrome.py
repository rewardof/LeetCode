"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
 Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution2:
    """
    bu meni yechimim, recursion ishlatgan holsa, ammo
    memory limitdan o'tib ketdi
    """

    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c for c in s if c.isalnum()).strip().lower()
        return cleaned == reverse_str(cleaned)


def reverse_str(s: str, i=0, reversed_s=''):
    if i == len(s):
        return reversed_s
    else:
        reversed_s = s[i] + reversed_s
        return reverse_str(s, i + 1, reversed_s)


class Solution3:
    def isPalindrome(self, s: str) -> bool:
        """
        my solution
        """
        cleaned = ''.join(c for c in s if c.isalnum()).strip().lower()
        for i in range(len(cleaned) // 2):
            if cleaned[i] == cleaned[-i - 1]:
                pass
            else:
                return False

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


s = 'eeccccbebaeeabebcccee'
print(Solution().isPalindrome(s))
