class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = float('-inf')
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right])*width)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea