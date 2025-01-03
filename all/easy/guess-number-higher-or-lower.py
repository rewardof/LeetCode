"""
374. Guess Number Higher or Lower
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        low, high = 1, n
        con = True
        while con:
            guess_number = (low + high) // 2
            result = guess(guess_number)
            if result == -1:
                high = guess_number - 1
            elif result == 1:
                low = guess_number + 1
            else:
                return guess_number


def guess(num: int):
    result = 6
    if num == result:
        return 0
    elif num > result:
        return -1
    else:
        return 1


print(Solution().guessNumber(10))
