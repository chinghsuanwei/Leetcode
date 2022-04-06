class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        flip = 0
        
        
        for _,c in enumerate(s):
            if c == '0':
                flip += 1
        
        ans = flip
        
        #11111
        #01111
        
        for i in range(len(s)):
            if s[i] == '0':
                flip -= 1
            else:
                flip += 1
                
            #print(flip)
            
            ans = min(ans, flip)
            
        return ans
                