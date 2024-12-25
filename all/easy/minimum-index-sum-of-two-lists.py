"""
599. Minimum Index Sum of Two Lists
"""
import heapq
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dict = {value: index for index, value in enumerate(list1)}
        min_index_sum = pow(10, 5)
        result = []
        for index, value in enumerate(list2):
            if value in list1_dict:
                index_sum = index + list1_dict[value]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [value]
                elif index_sum == min_index_sum:
                    result.append(value)
        return result


class Solution2:
    """
    best solution
    """
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        minHeap = []
        d = dict()

        for i, s in enumerate(list1):
            d[s] = i

        for i, s in enumerate(list2):
            if s in d:
                heapq.heappush(minHeap, (i + d[s], s))

        min_index_sum, s = heapq.heappop(minHeap)
        ans = [s]

        while minHeap and minHeap[0][0] == min_index_sum:
            ans.append(heapq.heappop(minHeap)[1])

        return ans




list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(Solution2().findRestaurant(list1, list2))



