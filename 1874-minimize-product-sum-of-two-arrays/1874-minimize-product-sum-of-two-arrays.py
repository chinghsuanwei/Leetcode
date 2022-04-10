import numpy as np

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        heapq.heapify(nums1)
        
        max_heap = []
        
        for val in nums2:
            heapq.heappush(max_heap, -val)
        
        ans = 0
        
        while len(nums1):
            ans += heapq.heappop(nums1) * heapq.heappop(max_heap) * -1
        
        
        return ans