class Solution:
    
    
                
                
            
    
    def splitArray(self, nums: List[int], m: int) -> int:
        #binary search
        
        def canSplit(nums: List[int], m: int, limit: int) -> bool:
        
            partition, size = 0, 0

            #1 2 3 4 5
            #take 5
            # 12 3 4 5
            # 12 3 

            #take 11
            # 1234

            # take 9
            # 123 4 5

            # take 8
            # 123 4 5

            for i,val in enumerate(nums):
                if val > limit:
                    return False

                partition += val #45 -> 9

                if partition > limit: # 9 > 8
                    size += 1 # 1
                    #print(size, partition)
                    partition = val # 5
                    

                    if size == m:
                        return False

            
            return True
        
        total = sum(nums)
        
        if total == 0:
            return 0
        
        lo, hi =  1, total
        
        while lo < hi:
            mid = lo + int((hi-lo)/2)
            
            #print("Try mid=", mid)
            if canSplit(nums, m, mid):
                hi = mid #11
            else:
                lo = mid + 1
                
        return lo
            
        
        