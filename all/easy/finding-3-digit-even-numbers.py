"""
2094. Finding 3-Digit Even Numbers
"""
from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits_c = Counter(digits)
        ans = []
        for i in range(100, 999, 2):
            c = Counter(str(i))
            if all(digits_c[int(key)] >= value for key, value in c.items()):
                ans.append(i)
        return ans


class Solution2:
    """
    AI solution(Bad)
    """

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits_c = Counter(digits)
        ans = set()

        # Generate three-digit numbers
        for h in digits:
            if h == 0:  # Hundreds place cannot be 0
                continue
            for t in digits:
                for u in digits:
                    if u % 2 == 1:  # Units digit must be even
                        continue
                    num = h * 100 + t * 10 + u
                    num_c = Counter([h, t, u])

                    # Ensure num can be formed using available digits
                    if all(digits_c[d] >= num_c[d] for d in num_c):
                        ans.add(num)

        return sorted(ans)


digits = [2, 1, 3, 0]
ans = [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
ans2 = [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
print(Solution().findEvenNumbers(digits))
