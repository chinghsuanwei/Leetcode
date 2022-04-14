class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        if grid[0][0] == 0 and n == 1:
            return 1
        
        dp = [[0 for x in range(n)] for x in range(n)]
        
        q = []
        
        q.append( (0, 0) )
        
        dp[0][0] = 1
        
        step = 2
        direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while len(q) > 0:
            
            # 8 direction
            
            size = len(q)
            
            for i in range(size):
                r, c = q.pop(0)
                
                for br, bc in direction:
                    new_r = r + br
                    new_c = c + bc
                    
                    if new_r == n-1 and new_c == n-1:
                        return step
                    
                    if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n or grid[new_r][new_c] == 1 or dp[new_r][new_c] != 0:
                        continue;
                    
                    q.append( (new_r, new_c) )
                    
                    dp[new_r][new_c] = step
                    
            step += 1
            
        return -1
        