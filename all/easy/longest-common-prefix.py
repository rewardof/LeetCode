from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs:
            new_prefix = ""
            for i in range(min(len(prefix), len(string))):
                if prefix[i] == string[i]:
                    new_prefix += prefix[i]
                else:
                    break

            prefix = new_prefix

        return prefix


# best solution
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for string in strs[1:]:  # Start comparing from the second string
            # Reduce prefix length until it matches the start of `string`
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:  # If prefix becomes empty
                    return ""

        return prefix


strs = ["cir", "car"]
result = Solution().longestCommonPrefix(strs)
print(result)
