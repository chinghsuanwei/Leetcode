class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        ans = 0
        
        for c in s:
            if c == '(':
                count += 1
            else:
                count -= 1
                
            if count < 0:
                count = 0
                ans += 1
        
        ans += count
        
        return ans