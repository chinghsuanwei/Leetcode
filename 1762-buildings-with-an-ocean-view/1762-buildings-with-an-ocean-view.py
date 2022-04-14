class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #reversely
        
        n = len(heights)
        res = [n-1]
        
        for i in range(n-2, -1, -1):
            
            if heights[i] > heights[ res[-1] ]:
                res.append(i)
        
        res.reverse()
        return res
            
            