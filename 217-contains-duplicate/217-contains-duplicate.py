class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        x = set(nums)
        if len(nums) == len(x):
            return False
        else:
            return True
