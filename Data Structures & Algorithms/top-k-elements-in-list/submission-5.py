class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 값:count를 갖는 dicts 만든다
        # 정렬후 슬라이싱으로 뽑는다,
        map = {};

        for x in nums:
            if x in map:
                map[x] += 1
            else:
                map[x] = 1

        counts = [x[0] for x in sorted(map.items(),key = lambda x:x[1])]

        return counts[len(counts)-k:]

        