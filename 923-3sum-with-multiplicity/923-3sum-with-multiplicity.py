class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        d = {}
        
        for val in arr:
            if val not in d:
                d[ val ] = 0
            d[ val ] += 1
        
        ans = 0
        mod = 10**9 + 7
        for num1 in d:
            for num2 in d:
                
                num3 = target - (num1 + num2)
                
                #print(num1, " ", num2, " ", num3, (num1 <= num2 <= num3))
                
                if not (num1 <= num2 <= num3):
                    continue
                
                if num3 in d:
                    
                    #print(num1, " ", num2, " ", num3)
                    # 1 1 1
                    # 1 2 2
                    # 2 2 1
                    # 2 1 2
                    # 1 2 3
                    
                    if num1 == num2 == num3:
                        if d[num1] >= 3:
                            ans += d[num1] * (d[num1]-1) * (d[num1]-2)//6
                    elif num1 == num2 or num1 == num3 or num2 == num3:
                        
                        #unique
                        a = num1 ^ num2 ^ num3
                        #dupliate
                        b = num1 ^ num2 ^ a
                        if a == b:
                            b = num1 ^ num3 ^ a
                        
                        #print(a, b)
                        
                        if d[b] >= 2:
                            ans += d[a] * d[b] * (d[b]-1)//2
                    else:
                        ans += d[num1] * d[num2] * d[num3]
                        
                    ans %= mod
                        
            
        return ans
                    
                    