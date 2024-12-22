from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        O(n*n) time and O(n) space complexity
        """
        i = 0
        for _ in range(len(nums)):
            if i == 0 or i > 0 and nums[i] != nums[i - 1]:
                pass
            else:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        O(n*n) time and O(n) space complexity
        """
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1

        return index


nums = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = Solution2().removeDuplicates(nums)
print(result)
