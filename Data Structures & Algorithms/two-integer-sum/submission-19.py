class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for idx,num in enumerate(nums):
            t = target - num

            if t in table:
                return [table[t],idx]

            table[num] = idx

        print(table)
        return [1,2]
            