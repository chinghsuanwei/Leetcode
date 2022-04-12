class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        # 2 2 2 2
        
        # 2 + 2 + 2
        
        # 1 1 1 1 1
        #   1 
        
        
        
        last_char = '?'
        
        ans = 0
        pre, cur = 0, 0  #1, 1
        # 1 1 1 1 1
        #   1 1 1 1
        
        # 2 2 2 2
        #   2 2 2
        
        for c in s:
            if last_char == c:
                cur += 1
            else:
                ans += min(pre, cur) #1, 1
                pre = cur
                cur = 1
                
                
                
            last_char = c
        
        ans += min(pre, cur)
        
            
        return ans
                