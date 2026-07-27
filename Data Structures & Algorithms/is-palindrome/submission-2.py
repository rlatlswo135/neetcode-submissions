class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        last = len(s)-1

        while(True):
            if start >= last:
                return True
            
            start_char = s[start].lower()
            last_char = s[last].lower()
            # 특수문자에 따른 인덱스 ++ -- 처리
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

        