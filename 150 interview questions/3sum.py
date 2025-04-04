"""
15. 3Sum
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = hashmap.get(num, []) + [index]
        result = []
        for i in range(len(nums)):
            summa = 0 - nums[i]
            j = i + 1
            while j < len(nums):
                third = summa - nums[j]
                if third in hashmap:
                    for index in hashmap[third]:
                        if index > j:
                            result.append([nums[i], nums[j], third])
                j += 1
        return result


from typing import List


class Solution2:
    """AI solution"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)


        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, n - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif summ > 0:
                    right -= 1
                else:
                    left += 1
        return result




nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
