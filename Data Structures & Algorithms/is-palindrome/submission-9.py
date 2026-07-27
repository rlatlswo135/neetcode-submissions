class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        last = len(s)-1

        while(start < last):

            while start < last and not s[start].isalnum():
                start += 1
            
            while start < last and not s[last].isalnum():
                last -= 1
            
            if s[start].lower() != s[last].lower():
                return False
            else:
                start += 1
                last -= 1
            
        return True

        