"""
Given a string s and an integer k, reverse the first k characters
for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and leave the other as original.
"""


class Solution2:
    """
    I solved myself, but it is inefficient
    """

    def reverseStr(self, s: str, k: int) -> str:
        limit = 0
        new_s = ''
        while limit < len(s):
            new_s += self.reverse(s, limit, limit + 2 * k, k)
            limit = limit + 2 * k
        return new_s

    def reverse(self, s, i, j, k):
        print(s[i:j])
        end = j
        if not j - i < k:
            j = j - k
        rev = ""
        for ch in s[i:j]:
            rev = ch + rev
        return rev + s[j:end]


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return ''.join(s)


s = "abcdsdfhsjakrdfoidfhdswlqsdfodsffnandas"
s1 = 'dcbasdjshfakofdridsdhfwlfdsqodnffsansad'
k = 3
print(Solution().reverseStr(s, k))
