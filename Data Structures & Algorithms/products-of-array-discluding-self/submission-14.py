import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        length = len(nums)

        left = [1] * length
        right = [1] * length

        for idx in range(1,length):
            left[idx] = left[idx-1] * nums[idx-1]

        for idx in range(length-2,-1,-1):
            right[idx] = right[idx+1] * nums[idx+1]

        for idx in range(0,length):
            result.append(left[idx] * right[idx])
        print(left,right)
        return result
        