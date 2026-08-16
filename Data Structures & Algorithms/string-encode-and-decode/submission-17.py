class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#Hello
        encode_str = ""
        for s in strs:
            encode_str += str(len(s)) + "#" + s
        return encode_str


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            index = ""
            while s[i] != "#":
                index += s[i]
                i += 1
            index = int(index)
            output.append(s[i + 1: i + 1 + index])
            i += index + 1
        return output


            
