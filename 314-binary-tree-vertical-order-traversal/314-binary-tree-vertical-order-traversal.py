# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS
        
        if not root:
            return []
        
        q = []
        
        ans = []
        
        min_offset = 10000000
        d = dict()
        q.append( (root, 0) ) 
        
        while len(q) > 0:
            size = len(q)
            
            for i in range(size):
                
                node, offset = q.pop(0)
                
                if not node:
                    continue
                
                if offset not in d:
                    d[offset] = list()
                
                d[offset].append(node.val)
                min_offset = min(min_offset, offset)
                
                if node.left:
                    q.append( (node.left, offset - 1) )
                if node.right:
                    q.append( (node.right, offset + 1) )
            
        
        idx = min_offset
        
        while idx in d:
            ans.append(d[idx])
            idx += 1
        
        return ans