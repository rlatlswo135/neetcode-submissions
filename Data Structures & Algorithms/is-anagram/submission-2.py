def check(s:str):
    dict = {};
    for c in s:
        dict[c] = dict.get(c,0) + 1;

    return dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_a = check(s);
        dict_b = check(t);

        if len(set(s) - set(t)) or len(set(t) - set(s)):
            return False


        for i in dict_a.keys():
            if i in dict_b:
                if dict_b[i] == dict_a[i]:
                    continue;
                else:
                    return False
            return False;

        return True

        
        