class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        D = {}
        
        res = 10 ** 9
        for i,val in enumerate(cards):
            if val not in D:
                D[val] = []
                D[val].append(i)
            else:
                res = min( res, i - D[val].pop(-1) + 1 ) 
                D[val].append(i)
                
                
        return -1 if res == 10 ** 9 else res