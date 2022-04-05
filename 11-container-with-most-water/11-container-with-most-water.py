class Solution:
    def maxArea(self, height: List[int]) -> int:
        #greedy algorithm
        
        n = len(height)
        l, r = 0, n-1
        
        maxArea = min(height[l], height[r])*(r-l)
        
        while l < r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
            maxArea = max(maxArea, min(height[l], height[r])*(r-l) )
            
        return maxArea