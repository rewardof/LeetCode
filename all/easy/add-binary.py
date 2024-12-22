"""
Given two binary strings a and b, return their sum as a binary string.

"""


class Solution:
    """
    my solution: 46% beats
    """
    def addBinary(self, a: str, b: str) -> str:
        length_a, length_b = len(a), len(b)
        result = ''
        addition = 0
        i, j = length_a - 1, length_b - 1
        while i >= 0 or j >= 0:
            sum = addition
            if i >= 0:
                sum += int(a[i])
            if j >= 0:
                sum += int(b[j])

            if sum < 2:
                result = str(sum) + result
                addition = 0
            elif sum == 2:
                addition = 1
                result = '0' + result
            else:
                addition = 1
                result = '1' + result
            i -= 1
            j -= 1
        if addition:
            return str(addition) + result
        else:
            return result


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length_a, length_b = len(a), len(b)
        result = []
        carry = 0
        i, j = length_a - 1, length_b - 1

        while i >= 0 or j >= 0 or carry:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1

            # Append the current digit to the result
            result.append(str(sum % 2))
            # Update carry
            carry = sum // 2

        # Reverse the result list and join to form the final string
        return ''.join(result[::-1])


a = "0"
b = "0"
result = Solution().addBinary(a, b)
print(result)
