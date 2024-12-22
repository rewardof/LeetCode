class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(len(haystack)):
            if haystack[i: i+length] == needle:
                return i
        return -1


# haystack = "sadbutsad"
# needle = "sad"
haystack = "leetcode"
needle = "leeto"
result = Solution().strStr(haystack, needle)
print(result)


