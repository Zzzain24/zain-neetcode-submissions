class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through the numbers
        # keep a list to track each number's occurence in the list
        # if a number already exists in this ocurrence list, return True
        # if reach outside the loop return False
        dups = set()
        for n in nums:
            if n in dups:
                return True
            dups.add(n)
        return False 