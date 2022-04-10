import numpy as np

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        min_heap = []
        max_heap = []
        
        for val in nums1:
            heapq.heappush(min_heap, val)
        
        for val in nums2:
            heapq.heappush(max_heap, -val)
        
        ans = 0
        
        while len(min_heap):
            ans += heapq.heappop(min_heap) * heapq.heappop(max_heap) * -1
        
        
        return ans