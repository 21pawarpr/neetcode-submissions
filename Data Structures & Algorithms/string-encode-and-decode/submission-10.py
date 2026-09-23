class Solution:

    def encode(self, strs: List[str]) -> str:
        # Put number of items in list, put number chars in string, 
        if len(strs) == 0:
            return ""
        encode_str = str(len(strs)) + "~"
        for s in strs:
            encode_str += str(len(s)) + "~" + s
        return encode_str
    def decode(self, s: str) -> List[str]:
        decode_strs = []
        if s == "":
            return decode_strs
        i = 0

        j = s.index("~", i)
        n = int(s[i:j])
        i = j + 1

        for _ in range(n):
            j = s.index("~", i)
            length = int(s[i:j])
            decode_strs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decode_strs

