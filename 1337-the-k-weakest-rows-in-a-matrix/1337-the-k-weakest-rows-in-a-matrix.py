class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        #simple sort
        #return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k];
        
        #simple sort either
        arr = []
        for idx, row in enumerate(mat) :
            arr.append( (sum(row), idx) )
            
        result = sorted(arr)[:k]
        
        result2 = []
        for idx, d in enumerate(result):
            result2.append(d[1])
            
        return result2
        