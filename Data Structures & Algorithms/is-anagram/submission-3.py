def check(s:str):
    dict = {};
    for c in s:
        dict[c] = dict.get(c,0) + 1;

    return dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = check(s);
        b = check(t);

        return a == b

        
        