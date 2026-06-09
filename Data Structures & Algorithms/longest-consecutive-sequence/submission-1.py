class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq = 0
        for n in nums:
            if n - 1 in nums:
                continue
            i = 0
            while (n + i) in nums:
                i += 1
            seq = max(seq, i)
        return seq

