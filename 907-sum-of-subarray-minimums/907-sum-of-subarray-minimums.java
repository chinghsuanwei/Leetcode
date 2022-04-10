class Solution {
    public int sumSubarrayMins(int[] arr) {
        
        int n = arr.length;
        
        
        int[] dp = new int[n];
        
        Stack<Integer> stack = new Stack<>();
        
        
        // -1 -1 1 2
        // 3   1 2 4
        
        // -1 -1 1 2 2
        // 3   1 2 5 4
        
        // 3   2 2+2 5+2  4*2 + 4
        // 
        
        // 3 2 2+2 4+ (2+2)
        
        
        int sum = 0;
        int MOD = 1000_000_000 + 7;
        stack.push(-1);
        
        for(int i=0; i<n; i++)
        {
            int val = arr[i];
            
            while(stack.size() > 1 && arr[ stack.peek() ] > val)
            {
                stack.pop();
            }
            
            int idx = stack.peek();
            
                
            stack.push(i);
            
            dp[i] += (i-idx)*val;
            
            if(idx != -1)
            {
                dp[i] += dp[idx];
                
            }
            
            sum += dp[i];
            sum %= MOD;
        }
        
        return sum;
        
    }
}