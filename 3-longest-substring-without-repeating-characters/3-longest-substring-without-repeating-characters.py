class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        p1, p2 = 0, 0
        result = 0
        counter = 0
        
        if s == " " or len(s) == 1:
            return 1
        
        while p2 < len(s):
            if s[p2] not in substring:
                substring[s[p2]] = 1
                counter += 1
                p2 += 1
            else:
                result = max(result, counter)
                substring.clear()
                counter = 0
                p1 += 1
                p2 = p1
        return max(result, counter)