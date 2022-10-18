# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return
        
        def bfs(root, depth):
            if len(result) < depth:
                result.append([])
            result[depth-1].append(root.val)
            if root.left:
                bfs(root.left, depth+1)
            if root.right:
                bfs(root.right, depth+1)
                             
            
            
            
        bfs(root, 1)
        result.reverse()
        return result