import collections

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        #scan from left to right
        
        l = []
        op = 0
        for val in nums:
            if len(l) % 2 == 0:
                l.append(val)
            else:
                if l[-1] != val:
                    l.append(val)
                else:
                    op += 1
                    
        
                    
        if len(l) % 2 != 0:
            l.pop()
            op += 1
        
        #should be even
        
        return op