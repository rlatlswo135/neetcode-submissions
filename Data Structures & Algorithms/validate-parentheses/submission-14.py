class Solution:
    def isValid(self, s: str) -> bool:
        dicts = {
            '(':')',
            '{':'}',
            '[':']',
        }

        stack = []

        for x in s:
            if x in dicts:
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False

                if x != dicts[stack.pop()]:
                    return False
        
        return len(stack) == 0
                

        
        