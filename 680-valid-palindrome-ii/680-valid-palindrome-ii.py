class Solution:
    def validPalindrome(self, s: str) -> bool:
        #from left and right
        
        #you can choose to delete left or right on, if both failed then failed
        
        start, end = 0, len(s)-1
        
        #abbcbca
        
        used = False
        success = True
        #two way
        while start < end:
            if s[start] != s[end]:
                if used:
                    success = False
                    break;
                
                if s[start+1] == s[end]:
                    start += 1
                    used = True
                else:
                    success = False
                    break;
                    
            start += 1
            end -= 1
        
        if success:
            return True
        
        
        used = False
        success = True
        
        start, end = 0, len(s)-1
        #two way
        while start < end:
            if s[start] != s[end]:
                if used:
                    return False
                
                if s[start] == s[end-1]:
                    end -= 1
                    used = True
                else:
                    return False
                
            start += 1
            end -= 1
            
        return True