class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        last = len(s)-1

        while(start < last):
            start_char = s[start]
            last_char = s[last]

            while start < last and not start_char.isalnum():
                start += 1
                start_char = s[start]
            
            while start < last and not last_char.isalnum():
                last -= 1
                last_char = s[last]
            
            if start_char.lower() != last_char.lower():
                return False
            else:
                start += 1
                last -= 1
            
        return True

        