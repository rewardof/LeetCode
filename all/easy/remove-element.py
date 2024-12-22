from typing import List


class Solution:
    """
    my solution
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            try:
                if nums[i] == val:
                    j = -1
                    while nums[j] == val:
                        nums.pop()
                    nums[i] = nums[-1]
                    nums.pop()
            except:
                pass
        return len(nums)


class Solution2:
    """
    CHatGPT solution
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
result = Solution2().removeElement(nums, val)
print(result)
