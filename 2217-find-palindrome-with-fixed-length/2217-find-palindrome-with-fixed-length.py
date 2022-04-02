class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        #10^7 
        
        #build dict for palinidrome
        
        # odd 101
        # even 1001, 1111
        
        # 9 10 9
        # 101, 111
        
        # 9 10 10 9
        # 101, 111
        
        #900
        # 9 10 10 10 9
        # 101, 111
        
        #100
        
        # 1 -> 9
        # 2 -> 9
        # 3 -> 90
        # 4 -> 90
        # 5 -> 900
        # 6 -> 900
        p = (intLength-1)//2
        
        
        d = dict()
        for i in range(1, intLength+1):
            d[i] = 9* (10**p)
        
        ans = []
        
        limit = d[intLength]
        for q in queries:
            
            if q > limit:
                ans.append(-1);
            else:
                # 1 -> 10
                # 2 -> 9* 10^0 = 90
                # 3 
                if intLength == 1:
                    ans.append(q)
                else:
                    num = (10 ** p) - 1
                    num += q
                    
                    #even
                    if intLength % 2 == 0:
                        ans.append( int(str(num) + str(num)[::-1]) )
                    else:
                        ans.append( int(str(num) + str(num)[:-1][::-1]) )
                        
        return ans
                    
        
        
        