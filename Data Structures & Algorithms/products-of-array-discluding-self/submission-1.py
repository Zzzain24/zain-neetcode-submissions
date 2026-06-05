class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix, postfix = 1, 1
        for i, n in enumerate(nums):
            output.append(prefix)
            prefix *= n
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output