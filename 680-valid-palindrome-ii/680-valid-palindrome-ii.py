class Solution:
    
    def _validPalindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
                    
            start += 1
            end -= 1
            
        return True
    
    def validPalindrome(self, s: str) -> bool:
        #from left and right
        
        #you can choose to delete left or right side, if both way failed, then it's impossible
        
        start, end = 0, len(s)-1
        
        #abbcbca
        
        #two way
        while start < end:
            if s[start] != s[end]:
                return self._validPalindrome(s, start+1, end) or self._validPalindrome(s, start, end-1)
                    
            start += 1
            end -= 1
            
        return True