class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        last = len(s)-1

        while(start < last):
            start_char = s[start].lower()
            last_char = s[last].lower()
            
            if start_char.isalnum() == False:
                start += 1
                continue

            if last_char.isalnum() == False:
                last -= 1
                continue
            
            if start_char != last_char:
                return False
            else:
                start += 1
                last -= 1
            
        return True

        