# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.g_sum = 0
        
        #right, mid, left
        
        # 4 6 7 8
        #8: 
        #
        
        def dfs(root: Optional[TreeNode]):
            
            if not root:
                return 0
            
            dfs(root.right)
            
            val = root.val
            root.val += self.g_sum
            self.g_sum += val
            
            
            dfs(root.left)
            
            
            
            
        
        dfs(root)
        
        return root
        
        
        
        