import collections

def sort_str(str):
    return "".join(sorted(str))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        table = {}
        outputs = []

        for i in strs:
            key = sort_str(i)

            if key not in table:
                table[key] = index
                outputs.append([i])

                index += 1
            else:
                outputs[table[key]].append(i)

        return outputs
            
        