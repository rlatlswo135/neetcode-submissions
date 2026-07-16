import collections

def get_key(str):
    counts = [0] * 26
    for i in str:
        counts[ord(i) - ord('a')] += 1
    
    return tuple(counts)

def sort_str(str):
    return "".join(sorted(str))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        table = {}
        outputs = []

        for i in strs:
            key = get_key(i)

            if key not in table:
                table[key] = index
                outputs.append([i])

                index += 1
            else:
                outputs[table[key]].append(i)

        return outputs
            
        