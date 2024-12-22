class Solution:
    """
    my own solution
    """
    def romanToInt(self, s: str) -> int:
        romans_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        roman_int = 0
        length = len(s)
        for i in range(length):
            if (i != length - 1) and s[i] < s[i+1]:
                roman_int -= romans_dict[s[i]]
            else:
                roman_int += romans_dict[s[i]]
        return roman_int


string = "LVIII"
result = Solution().romanToInt(string)
print(result)
