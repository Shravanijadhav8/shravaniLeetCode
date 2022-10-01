class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        hashmap = {}
        
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for i in t:
            if i not in hashmap:
                return False
            else:
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    hashmap.pop(i)
        return hashmap == {}
         