"""
189. Rotate Array
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        copy = nums.copy()
        for index, num in enumerate(nums):
            new_index = (index + k) % l
            nums[new_index] = copy[index]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        start = 0

        count = 0
        while count < l:
            current_index = 0
            current_value = nums[start]

            while True:
                next_index = (current_index + k) % l
                temp = nums[next_index]
                nums[next_index] = current_value
                current_value = temp
                current_index = next_index

                count += 1
                if start == current_index:
                    break

            start += 1
        print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(Solution().rotate2(nums, k))
