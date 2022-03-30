class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        #simple sort
        #return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k];
        
        
        
        #bucket sort
        buckets = [list() for _ in range(101)]
        
        for idx, row in enumerate(mat):
            j = bisect.bisect_left(row, 0, key=lambda idx: -idx)
            buckets[j].append(idx)
        
        result = []
        for i in range(101):
            result.extend(buckets[i])
            
        
        return result[:k]
        