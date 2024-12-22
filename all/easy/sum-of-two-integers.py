"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.


"""


class Solution:
    """AI solution"""
    def getSum(self, a: int, b: int) -> int:
        # Mask to handle 32-bit overflow
        mask = 0xFFFFFFFF
        # Maximum positive value for a 32-bit integer
        max_int = 0x7FFFFFFF

        while b != 0:
            # XOR gives the sum without carry
            sum_without_carry = a ^ b
            # AND followed by left shift gives the carry
            carry = (a & b) << 1

            # Apply mask to ensure 32-bit operations
            a = sum_without_carry & mask
            b = carry & mask

        # If the result is a negative number in 32-bit, convert it
        return a if a <= max_int else ~(a ^ mask)
