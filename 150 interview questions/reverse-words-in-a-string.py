"""
151. Reverse Words in a String
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        as_arr = s.split(' ')
        clean_arr = [word.strip() for word in as_arr if word]
        return ' '.join(reversed(clean_arr)).strip()



s = "a good   example"
print(Solution().reverseWords(s))
