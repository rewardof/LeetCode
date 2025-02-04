"""
2657. Find the Prefix Common Array of Two Arrays
"""
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        A_dict = {}
        B_dict = {}
        for i in range(n):
            A_dict[A[i]] = i
            B_dict[B[i]] = i
        for index, value in enumerate(A):
            count = 0
            for i in range(index + 1):
                if A[i] in B_dict and B_dict[A[i]] <= index:
                    count += 1

                ans[index] = count
        return ans

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        set_A = set()
        set_B = set()
        common = set()
        for i in range(n):
            set_A.add(A[i])
            set_B.add(B[i])
            if A[i] in set_B:
                common.add(A[i])
            if B[i] in set_A:
                common.add(B[i])
            ans[i] = len(common)
        return ans


A = [1, 3, 2, 4]
B = [3, 1, 2, 4]
print(Solution().findThePrefixCommonArray(A, B))
