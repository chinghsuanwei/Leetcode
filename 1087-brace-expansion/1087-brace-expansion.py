class Solution:
    def expand(self, s: str) -> List[str]:
        
        left_brace = -1
        
        l = []
        
        for i, c in enumerate(s):
            
            if c == '{':
                left_brace = i+1
            elif c == '}':
                #substr
                
                l.append( s[left_brace : i].split(",") )
                
                l[len(l)-1].sort()
                
                left_brace = -1
            else:
                
                if left_brace == -1:
                    l.append( list(c) )
        
        
        res = l[0]
        
        for i in range( 1, len(l) ):
            
            ans = []
            for str1 in res:
                for str2 in l[i]:
                
                    #print(str1)
                    #print(str2)
                    ans.append( str1 + str2 )
                    
            res = ans
            
        return res