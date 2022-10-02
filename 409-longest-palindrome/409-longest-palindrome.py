from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        pali = defaultdict(int)
        for i in s:
            pali[i] += 1
 #            if i not in pali:
#                 pali[i] = 1
#             else:
            
#         print(pali)
        result = 0
        #count = Counter(s)
        countOnes = 0
        countOdd = 0
        
        
        for i, val in pali.items():
            if val == 1:
                countOnes = 1
                
            elif val % 2 == 0:
                result += val
            else:
                countOdd = countOdd + (val-1)
        if countOnes == 0 and countOdd > 0:
            countOnes =1
                    
        
                
        return result+countOnes+countOdd
            
            
                
          
                