class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterate over nums and store numbers and counts to a map
        # k = 2
        # nums = [1, 2, 2, 3, 3, 3]
        # freq = {1: 1, 2: 2, 3: 3}
        # counts = [[], [1, 4], [2], [3], [], [], []]
        # the index value in counts represents the count of a number and the value in the list of lists represents the actual number 
        freq = {}
        counts = [[] for _ in range(len(nums) + 1)]
        output = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for key in freq:
            counts[freq[key]].append(key)
        for i in range(len(counts) - 1, 0, -1):
            for n in counts[i]:
                output.append(n)
                if len(output) == k:
                    return output