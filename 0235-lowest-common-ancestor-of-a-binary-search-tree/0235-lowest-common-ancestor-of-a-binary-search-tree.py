# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #as it is a BST we can search p and q depending on the root node
        # lowest will be on the left and highest will be on the right
        def dfs(root, p, q):
            if p.val < root.val and q.val < root.val:
                return dfs(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return dfs(root.right, p, q)
            else: return root
        return dfs(root,p,q)