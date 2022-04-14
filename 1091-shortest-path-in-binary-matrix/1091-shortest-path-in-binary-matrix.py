class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        if grid[0][0] == 0 and n == 1:
            return 1
        
        dp = [[0 for x in range(n)] for x in range(n)]
        
        q = []
        e_q = []
        
        q.append( (0, 0) )
        e_q.append( (n-1, n-1) )
        
        dp[0][0] = 1
        dp[-1][-1] = -1
        
        step = 2
        direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while len(q) > 0 and len(e_q) > 0:
            
            # 8 direction
            
            size = len(q)
            
            for i in range(size):
                r, c = q.pop(0)
                
                def checkLegalPosition(row, col) -> bool:
                        return row < 0 or row >= n or col < 0 or col >= n or grid[row][col] == 1
                
                for br, bc in direction:
                    new_r = r + br
                    new_c = c + bc
                    
                    if checkLegalPosition(new_r, new_c) or dp[new_r][new_c] > 0:
                        continue;
                        
                    if dp[new_r][new_c] < 0:
                        return step + abs(dp[new_r][new_c]) - 1
                    
                    q.append( (new_r, new_c) )
                    
                    dp[new_r][new_c] = step
            
            size = len(e_q)
            
            for i in range(size):
                r, c = e_q.pop(0)
                
                def checkLegalPosition(row, col) -> bool:
                        return row < 0 or row >= n or col < 0 or col >= n or grid[row][col] == 1
                
                for br, bc in direction:
                    new_r = r + br
                    new_c = c + bc
                    
                    if checkLegalPosition(new_r, new_c) or dp[new_r][new_c] < 0:
                        continue;
                        
                    if dp[new_r][new_c] > 0:
                        return step + abs(dp[new_r][new_c]) - 1
                    
                    e_q.append( (new_r, new_c) )
                    
                    dp[new_r][new_c] = -step
            
            step += 1
            
        return -1
        