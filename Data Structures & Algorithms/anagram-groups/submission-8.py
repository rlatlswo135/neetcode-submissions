import collections

def sort_str(str):
    return "".join(sorted(str))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for str in strs:
            key = "".join(sorted(str))

            if hash_map.get(key) is None:
                hash_map[key] = [str]
            else:
                hash_map[key].append(str)

        return [x for x in hash_map.values()]
            
        