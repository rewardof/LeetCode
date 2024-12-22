"""
Given an integer array nums, return the third distinct maximum number in this array.
 If the third maximum does not exist, return the maximum number.

"""
from typing import List


class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        i = 0
        nums = quick_sort_descending(nums)
        third_max = nums[0]
        print('nums', nums)
        for num in nums:
            if third_max != num:
                third_max = num
                i += 1
            if i == 2:
                return num
        return nums[0]


def quick_sort_descending(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x > pivot]  # Elements greater than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x < pivot]  # Elements less than the pivot
        return quick_sort_descending(left) + middle + quick_sort_descending(right)


class Solution3:
    """my solution"""

    def thirdMax(self, nums: List[int]) -> int:
        i = 0
        nums.sort(reverse=True)
        third_max = nums[0]
        print('nums', nums)
        for num in nums:
            if third_max != num:
                third_max = num
                i += 1
            if i == 2:
                return num
        return nums[0]


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max, second_max, third_max = None, None, None

        for num in nums:
            # Skip duplicates
            if num == first_max or num == second_max or num == third_max:
                continue

            # Update the three max variables
            if first_max is None or num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif second_max is None or num > second_max:
                third_max = second_max
                second_max = num
            elif third_max is None or num > third_max:
                third_max = num

        # Return third_max if it exists, otherwise first_max
        return third_max if third_max is not None else first_max


nums = [2,2,3,1]
print(Solution().thirdMax(nums))
