class Solution:
    def minWindow(self, s: str, t: str) -> str:
        satisfied_count, best_length, best_r, best_l, l, r = 0, len(s) + 1, 0, 0, 0, 0
        sMap, tMap = {}, {}
        valid_substring = False
        # populate map with character counts in t to compare to s substrings
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        required_count = len(tMap)

        while r < len(s):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            # helper function to check validtiy 
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                satisfied_count += 1

            if satisfied_count == required_count:
                if r - l + 1 < best_length:
                    best_length = r - l + 1
                    best_l = l
                    best_r = r
                while satisfied_count == required_count:
                    sMap[s[l]] -= 1
                    if s[l] in tMap and sMap[s[l]] == tMap[s[l]] - 1:
                        satisfied_count -= 1
                    l += 1
                    if satisfied_count == required_count:
                        if r - l + 1 < best_length:
                            best_length = r - l + 1
                            best_l = l
                            best_r = r
                    else:
                        break           
            r += 1
        if best_length == len(s) + 1:
            return ""
        else:
            # find the min value substring in output and return that string key 
            return s[best_l: best_r + 1]


