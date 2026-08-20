class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = 0
        nums = set(nums)
        for n in nums:
            if n - 1 in nums: 
                continue
            count = 0
            while n + count in nums:
                count += 1
            sequence = max(sequence, count)
        return sequence