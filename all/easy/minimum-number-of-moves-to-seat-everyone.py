"""
2037. Minimum Number of Moves to Seat Everyone
"""
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        min_moves = 0
        for i in range(len(seats)):
            min_moves += abs(seats[i] - students[i])
        return min_moves


seats = [3, 1, 5]
students = [2, 7, 4]
print(Solution().minMovesToSeat(seats, students))

