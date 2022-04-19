# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root: Optional[TreeNode], q: list):
            
            if not root:
                return
            
            dfs(root.left, q)
            
            q.append( root.val )
            
            dfs(root.right, q)
        
        q = []
        
        dfs(root, q)
        
        q.sort()
        
        
        def inorder(root: Optional[TreeNode], q: list):
            
            if not root:
                return
            
            inorder(root.left, q)
            
            root.val = q.pop(0)
            
            inorder(root.right, q)
            
        inorder(root, q)
        
        