class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        counts = []
        output = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for i in range(len(nums) + 1):
            counts.append([])
        for key in freq:
            counts[freq[key]].append(key)
        for i in range(len(counts) - 1, 0, -1):
            for j in counts[i]:
                output.append(j)
                if len(output) == k:
                    return output

        
         
        