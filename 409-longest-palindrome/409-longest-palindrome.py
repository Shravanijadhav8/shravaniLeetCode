from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
#         pali = defaultdict(int)
        
#         for i in s:
#             if i not in pali:
#                 pali[i] = 1
#             else:
#                 pali[i] += 1
#         print(pali)
        counter = defaultdict(int)
        for letter in s:
            counter[letter] += 1
        
        countEven = 0
        countOne = 0
        countOdd = 0
        for key, val in counter.items():
            if val % 2 == 0:
                countEven += val
            elif val == 1:
                countOne = 1
            else:
                countOdd = countOdd + (val - 1)
        if countOne == 0 and countOdd > 0:
            countOne = 1
        
        return countOne + countEven + countOdd
            
            
                
          
                