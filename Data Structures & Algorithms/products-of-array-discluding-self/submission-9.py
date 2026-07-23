import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        test = math.prod(nums)

        if test != 0:
            return [test // x for x in nums]

        dicts = {}
        result = []
        for idx,i in enumerate(nums):
            if i == 0:
                dicts[idx] = 0

        for idx,x in enumerate(nums):
            if dicts.get(idx,-1) < 0:
                result.append(0)
            else:
                sub_list = nums[:idx] + nums[idx+1:]
                result.append(math.prod(sub_list))
        
        return result
        