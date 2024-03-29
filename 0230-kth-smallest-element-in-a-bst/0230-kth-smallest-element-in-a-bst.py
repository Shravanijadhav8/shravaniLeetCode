# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root.val)
            if len(nodes) == k:
                return
            dfs(root.right)
            
        dfs(root)
        
        return nodes[k-1]