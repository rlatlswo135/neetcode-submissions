class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sub_list = []
        result_set = set()

        for num in sorted(nums):
            print(num)
            if sub_list == []:
                sub_list.append(num)
                continue
            
            pointer = sub_list[-1]
            if pointer == num:
                continue
            elif pointer + 1 == num:
                sub_list.append(num)
            else:
                result_set.add(len(sub_list))
                sub_list = [num]

        result_set.add(len(sub_list))
        return max(result_set)
        