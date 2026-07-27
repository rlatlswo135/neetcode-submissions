class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l_pointer = len(cleaned_s)-1

        for idx,c in enumerate(cleaned_s):
            print(cleaned_s)
            if c != cleaned_s[l_pointer]:
                return False
            
            l_pointer -= 1
        
        return True

        