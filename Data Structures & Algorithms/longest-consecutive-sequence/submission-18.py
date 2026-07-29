class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        num_set = set(nums)

        for x in num_set:
            if x-1 in num_set:
                continue

            pointer = x + 1
            count = 1
            while pointer in num_set:
                count += 1
                pointer += 1

            max_count = max(max_count,count)

        return max_count
        