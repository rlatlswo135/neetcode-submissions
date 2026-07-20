import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 값:count를 갖는 dicts 만든다
        # 정렬후 슬라이싱으로 뽑는다,
        result = []
        result_list = [0] * (len(nums) + 1)
        counter_map = collections.Counter(nums)

        for key,value in counter_map.items():
            if result_list[value]:
                result_list[value].append(key)
            else:
                result_list[value] = [key]

        for x in list(range(len(nums)+1))[::-1]:
            pick = result_list[x]
            if pick == 0:
                continue
            elif type(pick) == int:
                result.append(pick)
            else:
                pick_length = len(pick)
                if pick_length == k:
                    return pick
                elif pick_length < k:
                    result += pick

            if len(result) == k:
                return result

        # count를 index로 하고 num[]을 넣음 여기서 제일큰순으로 k 만큼 뽑아내야함
        print(result_list)
        return result

        