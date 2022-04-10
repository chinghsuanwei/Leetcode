class Solution {
    public int sumSubarrayMins(int[] arr) {
        
        int n = arr.length;
        
        
        int[] prefix = new int[n];
        
        Deque<int[]> dq = new LinkedList<int[]>();
        
        
        // -1 -1 1 2
        // 3   1 2 4
        
        // -1 -1 1 2 2
        // 3   1 2 5 4
        
        // 3   2 2+2 5+2  4*2 + 4
        // 
        
        // 3 2 2+2 4+ (2+2)
        
        
        int sum = 0;
        int MOD = 1000_000_000 + 7;
        
        for(int i=0; i<n; i++)
        {
            int val = arr[i];
            
            while(dq.size() > 0 && dq.getLast()[1] > val)
            {
                dq.pollLast();
            }
            
            int idx = -1;
            if(dq.size() > 0)
            {
                idx = dq.getLast()[0];
            }
                
            dq.addLast(new int[]{i, val});
            
            prefix[i] += (i-idx)*val;
            
            if(idx != -1)
            {
                prefix[i] += prefix[idx];
                
            }
            
            sum += prefix[i];
            sum %= MOD;
        }
        
        return sum;
        
    }
}