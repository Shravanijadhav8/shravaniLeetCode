class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        # x = set(nums)
        # if len(nums) == len(x):
        #     return False
        # else:
        #     return True
        
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                return True
        return False
