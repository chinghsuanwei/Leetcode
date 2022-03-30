class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        #simple sort
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k];
        
        #bucket sort
        #for 
        