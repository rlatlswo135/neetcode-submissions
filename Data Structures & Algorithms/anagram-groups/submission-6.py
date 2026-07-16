class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            normalized = "".join(sorted(s))
            if hashmap.get(normalized) is None:
                hashmap[normalized] = [s]
                continue
            hashmap[normalized].append(s)
        return [x for x in hashmap.values()]