# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = False
        def dfsHeight(root, level):
            nonlocal flag
            if not root: return level
            left = dfsHeight(root.left, level+1)
            right = dfsHeight(root.right, level+1)
            if abs(left-right) > 1: flag = True
            return max(left, right)
        
        dfsHeight(root, 0)
        return False if flag else True
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        unBalanced = False
        def height(root,level):
            nonlocal unBalanced
            if not root: return level
        
            left = height(root.left,level + 1)
            right = height(root.right,level + 1)
            if abs(left - right) > 1: unBalanced = True 
            return max(left,right) 
            
            
        height(root,0)
        return False if unBalanced else True
          """  
            
            