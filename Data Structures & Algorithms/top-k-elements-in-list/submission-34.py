import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        result_list = [[] for x in range(len(nums)+1)]
        counter_map = collections.Counter(nums)

        for key,value in counter_map.items():
                result_list[value].append(key)

        for x in reversed(range(len(nums)+1)):
            pick = result_list[x]
            if len(result) == k:
                return result
            else:
                result += pick

        return result

        