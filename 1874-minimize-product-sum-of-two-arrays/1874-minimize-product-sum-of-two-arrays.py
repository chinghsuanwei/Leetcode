class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        
        bucket1 = [0] * 101
        bucket2 = [0] * 101
        
        ans = 0
        
        for i in range(n):
            bucket1[ nums1[i] ] += 1
            bucket2[ nums2[i] ] += 1
            
        
        idx1 = 0
        idx2 = 100
        
        while n > 0:
            while bucket1[idx1] == 0:
                idx1 += 1;
            while bucket2[idx2] == 0:
                idx2 -= 1;
            
            bucket1[idx1] -= 1
            bucket2[idx2] -= 1
            
            ans += idx1 * idx2
            
            n -= 1
        
        
        return ans