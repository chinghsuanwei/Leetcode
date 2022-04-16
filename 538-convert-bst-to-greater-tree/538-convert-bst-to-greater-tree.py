# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #right, mid, left
        
        # 4 6 7 8
        #8: 
        #
        
        def dfs(root: Optional[TreeNode], parent_val: int):
            
            if not root:
                return 0
            
            right_val = dfs(root.right, parent_val)
            
            root.val += right_val #right
            child_val = root.val #self
            child_val += dfs(root.left, parent_val + child_val) #left
            
            root.val += parent_val
            
            
            #print(root.val)
            
            return child_val
            
        
        dfs(root, 0)
        
        return root
        
        
        
        