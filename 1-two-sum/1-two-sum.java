class Solution {
    public int[] twoSum(int[] nums, int target) {
        //hashmap
        // look up target - nums[i]
        // return the current index and the index of the entry in the map
        
        //9, 0
        //9-9 = 0, fail
        //9-0 = 9, success
        
        //3, 3  target = 6
        //6 - 3 = 3  dict: null
        //6 - 3 = 3  dict: (3, 0) return 0, 1
        
        HashMap<Integer, Integer> dict = new HashMap();
        
        // dict: {2, 0}
        // 9-7 = 2, dict: {2, 0}
        
        
        for(int i=0; i<nums.length; i++)
        {
            int num2 = target - nums[i];
            if(dict.get(num2) != null)
            {
                return new int[]{i, dict.get(num2)};
            }
            
            dict.put(nums[i], i);
        }
        
        return null;
    }
}