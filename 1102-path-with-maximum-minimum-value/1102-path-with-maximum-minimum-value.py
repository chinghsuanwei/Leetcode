class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        R, C = len(grid), len(grid[0])
        
        
        
        maxHeap = [(-grid[0][0], 0, 0)]
        
        seen = [[0 for _ in range(C)] for _ in range(R)]
        
        while maxHeap:
            val, y, x = heapq.heappop(maxHeap)
            
            if x == C - 1 and y == R - 1: return -val
            
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < C and 0 <= ny < R and not seen[ny][nx]:
                    seen[ny][nx] = 1
                    heapq.heappush(maxHeap, (max(val, -grid[ny][nx]), ny, nx))
                    
        
        return -1;