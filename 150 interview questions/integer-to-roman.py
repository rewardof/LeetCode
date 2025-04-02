"""
12. Integer to Roman
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        num_to_roman = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }
        result = ''
        i = 0
        for value, roman in num_to_roman.items():
            while num >= value:
                result += roman
                num -= value
        return result


num = 3914
print(Solution().intToRoman(num))
