class Solution:
    
    maximum = 1
    parent = None
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        #union find for every possible pos  union find n^2 + n^2
        
        n = len(grid)
        
        parent = [i for i in range(n*n)] # assign to itself
        size = [1 for i in range(n*n)] # assign to itself
        
        
        def find(x: int) -> int:
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(parent: List[int], size: List[int],  x: int, y: int):
            px, py = find(x), find(y)
                                                      
            if px != py:
                parent[py] = px
                size[px] += size[py]
                self.maximum = max(self.maximum, size[px])
        
        def unionAll(parent: List[int], size: List[int],  r: int, c: int):
            if r > 0 and grid[r-1][c] == 1:
                union(parent, size, r*n + c, (r-1)*n + c)
            if r < n-1 and grid[r+1][c] == 1:
                union(parent, size, r*n + c, (r+1)*n + c)
            if c > 0 and grid[r][c-1] == 1:
                union(parent, size, r*n + c, r*n + c - 1)
            if c < n-1 and grid[r][c+1] == 1:
                union(parent, size, r*n + c, r*n + c + 1)
        
        def to1D(r: int, c: int, n: int):
            return r*n + c;
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    unionAll(parent, size, r, c)
                    # if r > 0 and grid[r-1][c] == 1:
                    #     union(parent, size, r*n + c, (r-1)*n + c)
                    # if r < n-1 and grid[r+1][c] == 1:
                    #     union(parent, size, r*n + c, (r+1)*n + c)
                    # if c > 0 and grid[r][c-1] == 1:
                    #     union(parent, size, r*n + c, r*n + c - 1)
                    # if c < n-1 and grid[r][c+1] == 1:
                    #     union(parent, size, r*n + c, r*n + c + 1)
                    
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    #try insert 1
                    S = set()
                    if r > 0 and grid[r-1][c] == 1:
                        
                        S.add( find( to1D(r-1, c, n) ) )
                    if r < n-1 and grid[r+1][c] == 1:
                        
                        S.add( find( to1D(r+1, c, n) ) )
                        
                    if c > 0 and grid[r][c-1] == 1:
                        
                        S.add( find( to1D(r, c-1, n) ) )
                    if c < n-1 and grid[r][c+1] == 1:
                        
                        S.add( find( to1D(r, c+1, n) ) )
                    
                    total_size = 1
                    for e in S:
                        total_size += size[e]
                        
                    self.maximum = max(self.maximum, total_size)
        
        
        return self.maximum