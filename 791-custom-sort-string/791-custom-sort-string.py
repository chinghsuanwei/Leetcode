class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        D = dict()
        
        for c in s:
            if c not in D:
                D[c] = 1
            else:
                D[c] += 1
                
        #print(D)
        #sort those is order
        
        res = ""
        for c in order:
            if c in D:
                res += c * D[c]
                del D[c]
        
        for k in D:
            res += k * D[k]
            
        return res
        
        
        