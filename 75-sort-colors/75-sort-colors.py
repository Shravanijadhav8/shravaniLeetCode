from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashm = defaultdict(int)
        for i in nums:
            hashm[i] += 1
        temp = []
        temp.extend([0]*hashm[0])
        temp.extend([1]*hashm[1])
        temp.extend([2]*hashm[2])
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        #print(temp)
        
        
        
        