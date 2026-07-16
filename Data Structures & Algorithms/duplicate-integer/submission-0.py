class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set();

        for i in nums:
            if i in check_set:
                return True;
            else:
                check_set.add(i);

        return False;