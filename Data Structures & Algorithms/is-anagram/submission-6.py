class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram = [0] * 26
        for i in range(len(s)):
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')
            anagram[s_index] += 1
            anagram[t_index] -= 1
        return all(n == 0 for n in anagram)

        