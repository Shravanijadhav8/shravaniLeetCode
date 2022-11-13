# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        unBalanced = False
        def height(root,level):
            nonlocal unBalanced
            if not root: return level
        
            left = height(root.left,level + 1)
            right = height(root.right,level + 1)
            #print(f"root: {root.val} left:{left} right:{right}")
            if abs(left - right) > 1: unBalanced = True 
            return max(left,right) 
            
            
        height(root,0)
        return False if unBalanced else True
            
            
            