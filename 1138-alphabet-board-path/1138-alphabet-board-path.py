class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        cx, cy = 0, 0
        
        #only z is exception
        
        #if every character go to z, you need move to left first
        #if z go to every character, it need move up first
        
        #other characters are the same
        
        res = ""
        
        last_char = '?'
        for i,c in enumerate(target):
            
            def getCord(c: str):
                
                idx = ord(c) - ord('a')
                return idx%5, idx//5
            
            x, y = getCord(c)
            diff_x, diff_y = abs(cx - x), abs(cy - y)
            
            if c == 'z':
                #left first
                if diff_x > 0:
                    d = 'L'
                    res += d*diff_x
            
                if diff_y > 0:
                    d = 'D'
                    res += d*diff_y
                    
            elif last_char == 'z':
                if diff_y > 0:
                    d = 'U'
                    res += d*diff_y    
                
                if diff_x > 0:
                    d = 'R'
                    res += d*diff_x
            
            else:
                if diff_x > 0:
                    d = 'R' if x - cx > 0 else 'L'
                    res += d*diff_x
            
                if diff_y > 0:
                    d = 'D' if y - cy > 0 else 'U'
                    res += d*diff_y
                    
                    
            res += '!'
                
            
            
            last_char = c
            cx, cy = x, y
            
            
            

            
            
        return res