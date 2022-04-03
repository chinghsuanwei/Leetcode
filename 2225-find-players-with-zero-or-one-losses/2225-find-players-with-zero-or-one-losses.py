class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        d = dict()
        for i,l in enumerate(matches):
            if l[0] not in d:
                d[ l[0] ] = 0
            if l[1] not in d:
                d[ l[1] ] = 0
            d[ l[1] ] += 1
            
        list1 = []
        list2 = []
        for key, value in d.items():
            if value == 0:
                list1.append(key)
            elif value == 1:
                list2.append(key)
        
        list1.sort()
        list2.sort()
        
        return [list1, list2]
                
        