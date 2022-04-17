class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            
            def sumUp(s: str) -> int:
                total = 0
                for c in s:
                    total += int(c)
                    
                return total
            
            temp_str = ""
            while len(s) > k:
                substr = s[0:k]
                temp_str += str( sumUp(substr) )
                s = s[k:]
                
            if len(s) > 0:
                temp_str += str( sumUp(s) )
                
            s = temp_str
            
        
        return s