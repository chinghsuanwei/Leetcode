class Solution {
    public int maxProduct(int[] nums) {
        
        int n = nums.length;
        int l = nums[0];
        int r = nums[n-1];
        int max = Math.max(l, r);
        for(int i=1; i<n; i++)
        {
            l = (l == 0? 1 : l) * nums[i];
            r = (r == 0? 1 : r) * nums[n-1-i];
            
            max = Math.max(max, Math.max(l, r) );
        }
        
        return max;
    }
}