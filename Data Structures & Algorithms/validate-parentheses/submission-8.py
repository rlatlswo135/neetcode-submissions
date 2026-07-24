class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 > 0:
            return False

        dicts = {
            '(':')',
            '{':'}',
            '[':']',
        }

        stack = []

        for idx,x in enumerate(s):
            # open
            if type(dicts.get(x,-1)) == str:
                stack.append(x)
            # close
            else:
                if len(stack) == 0:
                    return False
                    
                pop = stack.pop()
                if x == dicts[pop]:
                    continue
                else:
                    return False
        
        return len(stack) == 0
                

        
        