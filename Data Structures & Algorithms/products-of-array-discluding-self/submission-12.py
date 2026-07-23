import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for idx,i in enumerate(nums):
            left = nums[:idx]
            right = nums[idx+1:]
            result.append(math.prod(left+right))

        return result
        