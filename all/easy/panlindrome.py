class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        num = x
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        return x == reversed_num


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10


a = Solution2().isPalindrome(1221312312313)
print(a)