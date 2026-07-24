class Solution:
    def isValid(self, s: str) -> bool:
        dicts = {
            '(':')',
            '{':'}',
            '[':']',
            ']':'',
            '}':'',
            ')':''
        }

        stack = []

        for x in s:
            if len(stack) == 0:
                stack.append(x)
            else:
                pop = stack.pop()
                if dicts[pop] == x:
                    continue
                stack += [pop,x]
        
        return len(stack) == 0

        
        