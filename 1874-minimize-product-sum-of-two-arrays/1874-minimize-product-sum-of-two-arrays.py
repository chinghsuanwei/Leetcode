import numpy as np

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        heapq.heapify(nums1)

        
        
        nums2 = (np.array(nums2) * -1).tolist()
        heapq.heapify(nums2)
        
        ans = 0
        
        while len(nums1):
            ans += heapq.heappop(nums1) * heapq.heappop(nums2) * -1
        
        
        return ans