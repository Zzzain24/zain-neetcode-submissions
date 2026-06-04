class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        length = ""
        i = 0
        while i < len(s):
            while s[i] != "#":
                length += s[i]
                i += 1
            print(length)
            decoded.append(s[i + 1: i + int(length) + 1])
            i += int(length) + 1
            length = ""
        return decoded
