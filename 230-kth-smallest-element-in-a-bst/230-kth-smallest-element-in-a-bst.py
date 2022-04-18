# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    ans = 0
    n = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder to find k element
        self.n = k
        
        def dfs(root: Optional[TreeNode]):
            
            if not root or self.n == 0:
                return
            
            
            dfs(root.left)
            
            #print(self.n)
            self.n -= 1
            if self.n == 0:
                self.ans = root.val
                
            dfs(root.right)
            
        dfs(root)
        
        return self.ans