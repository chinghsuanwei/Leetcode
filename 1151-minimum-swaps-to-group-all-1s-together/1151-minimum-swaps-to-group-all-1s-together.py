class Solution:
    def minSwaps(self, data: List[int]) -> int:
        width = sum(data)
        
        count1 = 0
        max1 = 0
        
        for r,d in enumerate(data):
            count1 += data[r]
            
            if r >= width:
                count1 -= data[r-width]
                
            max1 = max(max1, count1)
            
        return width - max1;