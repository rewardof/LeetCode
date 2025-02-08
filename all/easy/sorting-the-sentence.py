"""
1859. Sorting the Sentence
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([word[:-1] for word in sorted(s.split(' '), key=lambda x: x[-1])])

    def sortSentence2(self, s: str) -> str:
        as_list = s.split(' ')
        ans = [''] * len(as_list)
        for word in as_list:
            index = int(word[-1]) - 1
            ans[index] = word[:-1]
        return ' '.join(ans)


s = "is2 sentence4 This1 a3"
print(Solution().sortSentence2(s))
