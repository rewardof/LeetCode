"""
1491. Average Salary Excluding the Minimum and Maximum Salary
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return (sum(salary) - salary[0] - salary[-1]) // (len(salary) - 2)

