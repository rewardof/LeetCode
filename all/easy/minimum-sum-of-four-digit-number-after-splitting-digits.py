"""
2160. Minimum Sum of Four Digit Number After Splitting Digits
"""


class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while True:
            remain = num % 10
            digits.append(remain)
            num = (num - remain) // 10
            if num == 0:
                break
        digits.sort()
        num1 = 0
        num2 = 0
        for index, digit in enumerate(digits):
            if index % 2 == 0:
                num1 = num1 * pow(10, index // 2) + digit
            else:
                num2 = num2 * pow(10, (index - 1) // 2) + digit
        return num1 + num2

    def minimumSum2(self, num: int) -> int:
        digits = list(map(int, str(num)))
        digits.sort()
        num1 = ''
        num2 = ''
        for index, digit in enumerate(digits):
            if index % 2 == 0:
                num1 += str(digit)
            else:
                num2 += str(digit)
        return int(num1) + int(num2)

    def minimumSum3(self, num: int) -> int:
        digits = sorted(map(int, str(num)))
        return digits[0] * 10 + digits[2] + digits[1] * 10 + digits[3]


num = 2932
print(Solution().minimumSum3(num))
