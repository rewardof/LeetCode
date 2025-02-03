"""
1769. Minimum Number of Operations to Move All Balls to Each Box
"""
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        as_list = []
        for index, value in enumerate(boxes):
            if value == '1':
                as_list.append(index)
        ans = []
        for index, value in enumerate(boxes):
            summa = 0
            for i in as_list:
                summa += abs(i - index)
            ans.append(summa)
        return ans

    def minOperations2(self, boxes: str) -> List[int]:
        l = len(boxes)
        left_count = 0
        right_count = 0
        right_moves = 0
        left_moves = 0
        ans = [0] * l
        for i in range(l):
            ans[i] = left_moves
            if boxes[i] == '1':
                left_count += 1
            left_moves += left_count

        for i in range(l - 1, -1, -1):
            ans[i] += right_moves
            if boxes[i] == '1':
                right_count += 1
            right_moves += right_count
        return ans


boxes = "001011"
print(Solution().minOperations2(boxes))
