"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    
    
    
    def getPath(self, node: 'Node'):
        
        path = ""
        
        while node.parent != None:
            p = node.parent
            if p.left == node:
                path += 'L'
            else:
                path += 'R'
            
            node = p
        
        
        return path[::-1], node
    
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #record the path
        
        path_p, root = self.getPath(p)
        path_q, root = self.getPath(q)
        
        cur = root
        for i,c in enumerate(path_p):
            
            if i >= len(path_q):
                break
            
            if path_p[i] != path_q[i]:
                break
            
            if path_p[i] == 'L':
                cur = cur.left
            else:
                cur = cur.right
        
        
        return cur