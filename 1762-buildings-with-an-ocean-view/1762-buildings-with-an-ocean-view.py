class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #reversely
        
        n = len(heights)
        max_h = heights[ n-1 ]
        q = [n-1]
        
        for i in range(n-2, -1, -1):
            h = heights[i]
            if h > max_h:
                q.append(i)
            max_h = max(max_h, h)
        
        q.reverse()
        return q
            
            