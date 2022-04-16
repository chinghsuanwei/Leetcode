class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
          
#         1 2 3 4
#         5 6 7 8
#         9 a b c
#         d e f g
        
#         1 2 3 4
#         5 6 7 8
#         9 a b c
        
#         1 2 3 4
#         5 6 7 8
        
        
        # -> and down
        # down and ->
        
        q = [mat[0][0]]
        
        r, c = 0, 0
        
        m, n = len(mat), len(mat[0])
        
        bUpper = True
        while not (r+1 == m and c+1 == n):
            
            if bUpper:
                if r-1 >= 0 and c+1 < n:
                    r -= 1
                    c += 1
                else:
                    if c+1 < n:
                        c += 1
                    else:
                        r += 1
                    bUpper = False

            else:
                
                if r+1 < m and c-1 >= 0:
                    r += 1
                    c -= 1
                else:
                    if r+1 < m:
                        r += 1
                    else:
                        c += 1
                    bUpper = True
                
            #print(r, c)
            q.append(mat[r][c])
            
        return q