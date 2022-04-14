class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #23
        #25 2
        #29 6 4
        #35 12 10 6
        
        #20 2 3 4   9
        
        #2  4  7 
        
        #--
        #++++
        #+++++++
        #
        
        S = set()
        S.add(0)
        
        cSum = nums[0] % k
        
        S.add(cSum)
        zeros = 1 if nums[0] % k == 0 else 0
        
        n = len(nums)
        
        
        for i in range(1, n):
            
            
            cSum += nums[i]
            if nums[i] % k == 0:
                zeros += 1
                if zeros >= 2:
                    return True
            else:
                zeros = 0
                cSum %= k
                if cSum in S:
                    return True
            

            S.add(cSum)
            
            
        return False