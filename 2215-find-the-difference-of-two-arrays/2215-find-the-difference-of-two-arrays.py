class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        list1 = []
        list2 = []
        
        for val in nums1:
            if val not in set2:
                list1.append(val)
                set2.add(val)
                
        for val in nums2:
            if val not in set1:
                list2.append(val)
                set1.add(val)
                
                
        return [list1, list2]
            
        