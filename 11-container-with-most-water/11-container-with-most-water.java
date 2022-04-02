class Solution {
    public int maxArea(int[] height) {
        // [1,8,6,2,5,4,8,3,7]
        //  0 1 2 3 4 5 6 7 8
        
        // 8
        // 
        
        // 0    8
        
        // left_max, right_max
        // left_idx, right_idx
        
        int n = height.length;
        
        int l = 0;
        int r = n-1;
        
        int max = 0; 
        while(l < r)
        {
            max = Math.max(max, (r - l) * Math.min(height[l], height[r]));
            
            if(height[l] < height[r])
            {
                l++;
            }
            else
            {
                r--;
            }
        }
        
        return max;
    
    }
}