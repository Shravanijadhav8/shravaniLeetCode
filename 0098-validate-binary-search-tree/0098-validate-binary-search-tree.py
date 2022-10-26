# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            nonlocal prev
            if not root: return True
            if not dfs(root.left): return False
            if root.val <= prev:
                return False
            prev = root.val
            return dfs(root.right)
        
        prev = float('-inf')
        return dfs(root)
    
        
        
            
        
#         nodes = []
        
#         def dfs(root):
#             if not root:
#                 return
#             dfs(root.left)
#             nodes.append(root.val)
#             dfs(root.right)
#         dfs(root)
        
#         for i in range(len(nodes)-1):
#             if nodes[i+1] <= nodes[i]:
#                 return False
#         return True