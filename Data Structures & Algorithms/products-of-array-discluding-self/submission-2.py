class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefix = 1
        for i, n in enumerate(nums):
            output[i] = prefix
            prefix *= n
        postfix = 1
        for i in range(len(output) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
        