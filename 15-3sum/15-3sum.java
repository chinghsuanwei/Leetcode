class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        Set<Integer> set = new HashSet<Integer>();
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        int count = 0;
        for(int i=0; i<nums.length; i++)
        {
            set.add(nums[i]);
            if(nums[i] == 0) {
                count++;
            }
        }
        
        if(count >= 3)
        {
            ans.add(Arrays.asList(0, 0, 0));
        }
                    
        
        int first_num = -1000_000;
        
        for(int i=0; i<nums.length; i++)
        {
            if(first_num == nums[i] || nums[i] == 0) continue;
            
            first_num = nums[i];
            
            
            int second_num = -1000_000;
            for(int j=i+1; j<nums.length && ((nums[j] <= 0) == (nums[i] <= 0)); j++)
            {
                if(second_num == nums[j]) continue;
                
                second_num = nums[j];
                int thrid_num = -(first_num + second_num);
                if( set.contains( thrid_num ) )
                {
                    ans.add(Arrays.asList(first_num, second_num, thrid_num));    
                }
                
            }
        }
        

        return ans;
        
    }
}