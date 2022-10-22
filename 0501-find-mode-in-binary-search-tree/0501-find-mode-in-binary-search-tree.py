# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        node = []
        prev = None
        currCount = 0
        maxCount = 0
        
        def dfs(root):
            nonlocal node
            nonlocal prev
            nonlocal maxCount
            nonlocal currCount
            if not root: return
            dfs(root.left)
            if prev == root.val:
                currCount += 1
            else:
                currCount = 1
            if currCount == maxCount:
                node.append(root.val)
            if currCount > maxCount:
                node = [root.val]
                maxCount = currCount
            prev = root.val
            
            
            dfs(root.right)
        dfs(root)
        return node
    
    
    
#     Inorder traversal of a BST will find the nodes in ascending order. So just compare the current node to the previous, and if they match, increase the current count of duplicate values by 1. If they don't match, reset the current count to 1. Compare the current count to the max count found so far. If they match, append the current value to the result list. If the current count of duplicates exceeds the max count, create a new result list with just the current value.

# class Solution(object):
#     prev = None
#     max_count = 0
#     current_count = 0 
#     result = []

#     def findMode(self, root):
#         self.dfs(root)
#         return self.result

#     def dfs(self, node):
#         if not node: return
#         self.dfs(node.left)
#         self.current_count = 1 if node.val != self.prev else self.current_count + 1
#         if self.current_count == self.max_count:
#             self.result.append(node.val)
#         elif self.current_count > self.max_count:
#             self.result = [node.val]
#             self.max_count = self.current_count
#         self.prev = node.val
#         self.dfs(node.right)