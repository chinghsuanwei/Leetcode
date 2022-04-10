class Solution:
    def minimizeResult(self, expression: str) -> str:
        # brute force
        
        #left 
        #(999
        #9(99
        
        nums = expression.split("+")
        print(nums)
        
        left_exp = []
        right_exp = []
        
        
        for i in range(len(nums[0])):
            if i == 0:
                left_exp.append( nums[0][:i] + '(' + nums[0][i:] )
            else:
                left_exp.append( nums[0][:i] + '*(' + nums[0][i:] )
            
        for i in range(1, len(nums[1])+ 1):
            if i == len(nums[1]):
                right_exp.append( nums[1][:i] + ')' + nums[1][i:] )
            else:
                right_exp.append( nums[1][:i] + ')*' + nums[1][i:] )
                
        print(left_exp)
        print(right_exp)
        
        exps = [x + "+" + y for x in left_exp for y in right_exp]
    
        idx = -1
        min_val = sys.maxsize
        for i,exp in enumerate(exps):
            val = eval(exp)
            if min_val > val:
                min_val = val
                idx  = i
        
        
        return exps[idx].replace("*", "")