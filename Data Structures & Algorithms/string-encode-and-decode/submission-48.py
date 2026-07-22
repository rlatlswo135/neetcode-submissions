MARKER = "&"
C_MARKER = "-"
class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        len_list = "".join([f"{len(x)}{C_MARKER}" for x in strs])
        serial = "".join(strs)

        return f"{len_list}{MARKER}{serial}"

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        maker_idx = s.find(MARKER)

        result = []
        pointer = 0
        c_pointer = 0

        strs = s[maker_idx+1:]
        counts = s[:maker_idx]

        for idx,count in enumerate(counts):
            if count == C_MARKER:
                i_count = int(counts[c_pointer:idx])
                word = strs[pointer:pointer + i_count]

                result.append(word)
                c_pointer = idx + 1
                pointer += i_count
                

        return result
