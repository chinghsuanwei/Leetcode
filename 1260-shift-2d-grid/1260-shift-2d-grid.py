class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        q = []
        
        
        
        m = len(grid)
        n = len(grid[0])
        size = m*n
        k %= m*n
        
        if k == 0:
            return grid
        
        for r in range(m):
            for c in range(n):
                q.append(grid[r][c])
        
        
        for i in range(size):
            idx = (k + i) % size
            r = idx // n
            c = idx % n
            
            grid[r][c] = q[i]
            
                
                
        return grid
            