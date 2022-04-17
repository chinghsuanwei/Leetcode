class Node:
        def __init__(self, c: str):
            self.c = c
            self.nodes = []
class Solution:
    
    
    res = 1
    
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = {}
        
        root_id = -1
        for i,c in enumerate(s):
            if i not in graph:
                graph[i] = Node(c)
            
            pi = parent[i]
            
            if pi == -1:
                root_id = i
                continue
                
            if pi not in graph:
                graph[ pi ] = Node( s[ pi ] )
                
            graph[ pi ].nodes.append( graph[i] )
                
        
        #dfs
        def dfs(root: 'Node') -> int:
            
            if not root:
                return 0
            
            
            
            q = []
            for node in root.nodes:
                
                length = dfs(node)
                if node.c != root.c:
                    q.append( length )    
                
            
            q.sort(reverse = True)
            
            if len(q) >= 2:
                self.res = max(self.res,  q[0] + q[1] + 1)
            elif len(q) == 1:
                self.res = max(self.res,  q[0] + 1)
            
            print(q)
            
            return q[0]+1 if len(q) > 0 else 1
        
        
        dfs(graph[root_id])
        
        return self.res