class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # pwwkew
        #    lrr
        dups = set()
        l, longest = 0, 0
        for r, c in enumerate(s):
            while c in dups:
                dups.remove(s[l])
                l += 1
            dups.add(c)
            longest = max(longest, r - l + 1)
        return longest 
            
            