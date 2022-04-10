class Solution:
    def largestInteger(self, num: int) -> int:
        
        even = []
        odd = []
        
        i = num
        
        while i > 0:
            
            if i % 2 == 0:
                even.append(i % 10)
            else:
                odd.append(i % 10)
                
            i //= 10
        
        even.sort(reverse = True)
        odd.sort(reverse = True)

        #90000
        
        str_num = str(num)
        
        ans = str()
        for i,c in enumerate(str_num):
            
            if int(c) % 2 == 0:
                ans += str(even[0])
                even.pop(0)
            else:
                ans += str(odd[0])
                odd.pop(0)
            
            
                
        
        return int(ans)