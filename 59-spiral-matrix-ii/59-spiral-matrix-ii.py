class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        end = n*n
        
        matrix = [[0 for x in range(n)] for y in range(n)]
        
        #right, down, left, up
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        
        
        
        r, c = 0, 0
        matrix[0][0] = 1
        
        num = 2
        while num <= end:
                        
            #hit the border
            new_r = r + direction[d][0]
            new_c = c + direction[d][1]
            
            if new_r < 0 or new_c < 0 or new_r >= n or new_c >= n or matrix[new_r][new_c] != 0:
                #change direction
                d += 1
                d %= 4
                new_r = r + direction[d][0]
                new_c = c + direction[d][1]
            
            #print(r, c);
            r = new_r
            c = new_c
            
            matrix[r][c] = num
            num += 1
            
                
            
        return matrix
            
            