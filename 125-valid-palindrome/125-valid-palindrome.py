class Solution:
    def isPalindrome(self, s: str) -> bool:
        list = []
        for i in s.lower():
            if i.isalnum():
                list.append(i)
        print(list)
        return list == list[::-1]