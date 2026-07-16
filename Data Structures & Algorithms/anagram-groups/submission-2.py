import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = []

        for i in strs:
            q = 0
            s_i = collections.Counter(i)

            for x in outputs:
                if s_i == collections.Counter(x[0]):
                    x.append(i)
                    q += 1
                    break
            
            if q == 0:
                outputs.append([i])
            
        return outputs
            
        