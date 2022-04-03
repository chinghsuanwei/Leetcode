class Solution:
    
    def canGiveAllCandy(self, candies: List[int], k: int, size: int) -> bool:
        
        if size == 0:
            return True
        
        number = 0
        
        for v in candies:
            number += v // size
        
        
        return number >= k
    
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        lo, hi = 0, 10 ** 7+1
        
        while lo < hi:
            mid = lo + (hi-lo)//2
            
            #print(mid)
            
            if self.canGiveAllCandy(candies, k, mid):
                lo = mid + 1
            else:
                hi = mid
                
        
        return lo-1