class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        output = []
        for s in strs:
            key = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                key[index] += 1
            key = tuple(key)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        for key in anagrams:
            output.append(anagrams[key])
        return output