"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
from typing import List


class Solution:
    """
    my solution
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        while index > 0 and digits[index] == 9:
            digits[index] = 0
            index -= 1
        if index == 0 and digits[index] == 9:
            digits[index] = 1
            digits.append(0)
        else:
            digits[index] = digits[index] + 1
        return digits


class Solution2:
    """ChatGPT solution"""
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):  # Iterate from the last digit backward
            if digits[i] < 9:  # If the digit is not 9, increment and return
                digits[i] += 1
                return digits
            digits[i] = 0  # If the digit is 9, set it to 0 and continue

        # If all digits were 9, prepend 1 to the list
        return [1] + digits


digits = [9, 9, 9, 9]
result = Solution().plusOne(digits)
print(result)