# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root):
            if not root: return False
            
            left = lca(root.left)
            right = lca(root.right)
            
            if left and right: 
                print(root.val)
                return root
            
            if root == p or root == q:
                if left or right: 
                    print(root.val)
                    return root
                else: 
                    return True
            return left or right
        return lca(root)
        
            