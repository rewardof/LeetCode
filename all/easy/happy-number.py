"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # To keep track of numbers we've already seen

        while n != 1:
            summa = 0
            while n > 0:
                digit = n % 10
                summa += digit * digit
                n //= 10
            n = summa
            if n in seen:  # Cycle detected
                return False
            seen.add(n)

        return True  # n == 1 means it's a happy number


n = 2
print(Solution().isHappy(n))

