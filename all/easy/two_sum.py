from typing import List


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store value and index pairs
        num_to_index = {}
        for index, value in enumerate(nums):
            complement = target - value

            if complement in num_to_index:
                return [num_to_index[complement], index]

            num_to_index[value] = index


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, num in enumerate(nums):
            remain = target - num
            if remain in nums_dict:
                return [nums_dict[remain], index]
            else:
                nums_dict[num] = index


nums = [1, 3, 2, 6, 7, 8]
target = 8

answer = Solution().twoSum(nums, target)
print(answer)