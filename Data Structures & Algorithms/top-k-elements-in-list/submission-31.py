import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        result_list = [[] for x in range(len(nums)+1)]
        counter_map = collections.Counter(nums)

        for key,value in counter_map.items():
                result_list[value].append(key)

        for x in list(range(len(nums)+1))[::-1]:
            pick = result_list[x]
            if len(result) == k:
                return result
            elif len(pick) == k:
                return pick
            else:
                result += pick

        # count를 index로 하고 num[]을 넣음 여기서 제일큰순으로 k 만큼 뽑아내야함
        return result

        