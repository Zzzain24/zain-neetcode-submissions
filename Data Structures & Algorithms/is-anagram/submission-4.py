class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap, tMap = {}, {}
        for i, l in enumerate(s):
            sMap[l] = sMap.get(l, 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        return sMap == tMap 
        