class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = range(len(nums))

        for x in ls:
            for i in range(x+1,len(nums)):
                if nums[x] + nums[i] == target:
                    return [x,i]