"""
Problem Intuition :
The problem asks us to check if there are any duplicate values in an array. The simplest way to identify duplicates is to keep track of all elements we’ve seen so far. If we encounter an element already tracked, it’s a duplicate. To do this efficiently, we can use a hash set because:

Checking if an element exists in a set is ( O(1) ) on average.
Adding elements to a set is ( O(1) ) on average.
Using a hash set avoids the need to modify the input array, making the solution clean and reliable.

Code Idea :
Use a hash set to store elements we’ve seen so far.
Iterate through the array:
If an element is already in the set, return true (duplicate found).
Otherwise, add the element to the set.
If we finish iterating without finding duplicates, return false.
Algorithm :
Initialize a hash set:
This set will store all the elements we've encountered so far.
Iterate through the array:
For each element:
If the element exists in the set, return true (a duplicate is found).
Otherwise, add the element to the set.
Return false:
If the loop completes without finding duplicates, it means all elements are distinct.
"""

from typing import List


class Solution:
    """my solution"""

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for value in nums:
            if value in nums_dict:
                return True
            else:
                nums_dict[value] = 1
        return False


# best solution
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


def containsDuplicate(nums):
    nums.sort()  # Sort the array
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:  # Check consecutive elements
            return True
    return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result = Solution().containsDuplicate(nums)
print(result)
