import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for str in strs:
            key = "".join(sorted(str))

            if hash_map.get(key) is None:
                hash_map[key] = [str]
            else:
                hash_map[key].append(str)

        return list(hash_map.values())
            
        