# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root.val)
            dfs(root.right)
        dfs(root)
        
        for i in range(len(nodes)-1):
            if nodes[i+1] <= nodes[i]:
                return False
        return True